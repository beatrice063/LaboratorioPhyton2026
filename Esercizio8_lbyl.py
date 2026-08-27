import json
import random

FILE_PAROLE = "parole.json"
TENTATIVI_MAX = 6
ALFABETO = "abcdefghijklmnopqrstuvwxyz"


def carica_parola(percorso):
    """Carica la lista di parole dal file JSON e ne sceglie una a caso."""

    # Apertura del file: la teoria fornita non offre un modo LBYL per
    # verificarne l'esistenza prima di aprirlo (richiederebbe try/except,
    # tecnica EAFP), quindi si assume che il file esista.
    with open(percorso, "r") as file_parole:
        dati = json.load(file_parole)

    # --- LBYL CONTROLLO 1: presenza della chiave "parole" ---
    if "parole" not in dati.keys():
        print("Errore: il file JSON non contiene la chiave 'parole'.")
        return None

    lista_parole = dati["parole"]

    # --- LBYL CONTROLLO 2: lista non vuota ---
    if len(lista_parole) == 0:
        print("Errore: la lista delle parole è vuota.")
        return None

    # Scelta della parola casuale: stesso pattern usato per le 8 Regine
    # (Lezione 7) e ripreso in Lezione 9 per l'uso del modulo random.
    generatore = random.Random()
    indici = list(range(len(lista_parole)))
    generatore.shuffle(indici)
    parola = lista_parole[indici[0]]

    return parola


def mostra_stato(parola, lettere_indovinate, lettere_tentate, tentativi_rimasti):
    """Visualizza a schermo lo stato attuale della partita."""

    # Costruzione manuale della parola mascherata
    mascherata = ''
    for lettera in parola:
        if lettera in lettere_indovinate:
            mascherata = mascherata + lettera + ' '
        else:
            mascherata = mascherata + '_ '

    # Costruzione manuale dell'elenco delle lettere già tentate
    elenco_tentate = ''
    for lettera in lettere_tentate:
        elenco_tentate = elenco_tentate + lettera + ' '

    print(f"\nParola: {mascherata}")
    print(f"Tentativi rimasti: {tentativi_rimasti}")
    if len(lettere_tentate) == 0:
        print("Lettere già tentate: (nessuna)")
    else:
        print(f"Lettere già tentate: {elenco_tentate}")


def parola_completata(parola, lettere_indovinate):
    """Controlla se tutte le lettere della parola sono state indovinate."""
    completa = True
    for lettera in parola:
        if lettera not in lettere_indovinate:
            completa = False
    return completa


def gioca(parola):
    """Gestisce il ciclo di gioco applicando rigorosamente controlli LBYL."""

    lettere_indovinate = set()
    lettere_tentate = set()
    tentativi_rimasti = TENTATIVI_MAX

    while tentativi_rimasti > 0:

        # --- LBYL CONTROLLO: condizione di vittoria ---
        if parola_completata(parola, lettere_indovinate):
            print(f"\nHai indovinato! La parola era '{parola}'.")
            return

        mostra_stato(parola, lettere_indovinate, lettere_tentate, tentativi_rimasti)

        scelta = input("Inserisci una lettera o prova l'intera parola: ")

        # --- LBYL CONTROLLO: input vuoto ---
        if len(scelta) == 0:
            print("Non hai inserito alcun carattere!")
            continue

        if len(scelta) == 1:

            # --- LBYL CONTROLLO: carattere alfabetico ---
            if scelta not in ALFABETO:
                print("Inserisci una lettera valida (a-z).")
                continue

            # --- LBYL CONTROLLO: tentativo duplicato ---
            if scelta in lettere_tentate:
                print(f"Hai già provato la lettera '{scelta}'.")
                continue

            lettere_tentate.add(scelta)

            # --- LBYL CONTROLLO: esito della lettera ---
            if scelta in parola:
                lettere_indovinate.add(scelta)
                print("Lettera corretta!")
            else:
                tentativi_rimasti -= 1
                print("Lettera sbagliata!")

        else:
            # --- LBYL CONTROLLO: lunghezza compatibile con la parola segreta ---
            if len(scelta) != len(parola):
                print("Input non valido: lunghezza diversa dalla parola segreta.")
                continue

            # --- LBYL CONTROLLO: corrispondenza della parola ---
            if scelta == parola:
                print(f"\nFantastico! Hai indovinato l'intera parola: '{parola}'.")
                return
            else:
                tentativi_rimasti -= 1
                print("Parola sbagliata!")

    print(f"\nHai esaurito i tentativi. La parola era '{parola}'.")


def main():
    parola = carica_parola(FILE_PAROLE)

    # --- LBYL CONTROLLO: esito del caricamento ---
    if parola is not None:
        gioca(parola)
    else:
        print("Impossibile avviare il gioco a causa di errori nel file.")


main()
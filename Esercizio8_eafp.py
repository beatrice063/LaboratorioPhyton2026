import json
import random

FILE_PAROLE = "parole.json"
TENTATIVI_MAX = 6


def carica_parola(percorso):
    """Carica la lista di parole e ne sceglie una a caso, in stile EAFP:
    si prova direttamente l'operazione e si gestisce l'eventuale eccezione."""

    # --- EAFP: lettura del file ---
    try:
        with open(percorso, "r") as file_parole:
            dati = json.load(file_parole)
    except FileNotFoundError:
        print(f"Errore: il file '{percorso}' non esiste.")
        return None

    # --- EAFP: accesso alla chiave "parole" e scelta della parola casuale ---
    try:
        lista_parole = dati["parole"]
        generatore = random.Random()
        indici = list(range(len(lista_parole)))
        generatore.shuffle(indici)
        parola = lista_parole[indici[0]]
    except KeyError:
        print("Errore: il file JSON non contiene la chiave 'parole'.")
        return None
    except IndexError:
        print("Errore: la lista delle parole è vuota.")
        return None

    return parola


def mostra_stato(parola, lettere_indovinate, lettere_tentate, tentativi_rimasti):
    """Visualizza lo stato corrente della partita, in stile EAFP."""

    mascherata = ''
    for lettera in parola:
        try:
            lettere_indovinate[lettera]
            mascherata = mascherata + lettera + ' '
        except KeyError:
            mascherata = mascherata + '_ '

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
    """Controlla, in stile EAFP, se tutte le lettere sono state indovinate."""
    completa = True
    for lettera in parola:
        try:
            lettere_indovinate[lettera]
        except KeyError:
            completa = False
    return completa


def gioca(parola):
    """Ciclo principale del gioco, scritto in stile EAFP puro."""

    lettere_indovinate = {}
    lettere_tentate = {}
    tentativi_rimasti = TENTATIVI_MAX

    # Dizionario di appoggio con le lettere realmente presenti nella parola
    # (stesso pattern EAFP visto in Lezione 12 per contare occorrenze)
    lettere_della_parola = {}
    for lettera in parola:
        try:
            lettere_della_parola[lettera] += 1
        except KeyError:
            lettere_della_parola[lettera] = 1

    # Dizionario con un'unica chiave valida: la parola corretta stessa
    parola_valida = {parola: True}

    while tentativi_rimasti > 0:

        if parola_completata(parola, lettere_indovinate):
            print(f"\nHai indovinato! La parola era '{parola}'.")
            return

        mostra_stato(parola, lettere_indovinate, lettere_tentate, tentativi_rimasti)

        scelta = input("Inserisci una lettera o prova l'intera parola: ")

        if len(scelta) == 0:
            continue

        if len(scelta) == 1:

            # --- EAFP: la lettera è già stata tentata? ---
            try:
                lettere_tentate[scelta]
            except KeyError:
                lettere_tentate[scelta] = True

                # --- EAFP: la lettera appartiene alla parola? ---
                try:
                    lettere_della_parola[scelta]
                except KeyError:
                    tentativi_rimasti -= 1
                    print("Lettera sbagliata!")
                else:
                    lettere_indovinate[scelta] = True
                    print("Lettera corretta!")
            else:
                print(f"Hai già provato la lettera '{scelta}'.")

        else:
            # --- EAFP: la parola inserita è quella corretta? ---
            try:
                parola_valida[scelta]
            except KeyError:
                tentativi_rimasti -= 1
                print("Parola sbagliata!")
            else:
                print(f"\nFantastico! Hai indovinato l'intera parola: '{parola}'.")
                return

    print(f"\nHai esaurito i tentativi. La parola era '{parola}'.")


def main():
    parola = carica_parola(FILE_PAROLE)

    if parola is not None:
        gioca(parola)
    else:
        print("Impossibile avviare il gioco a causa di un errore nel file.")


main()
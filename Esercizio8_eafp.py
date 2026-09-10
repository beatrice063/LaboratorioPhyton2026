#NOME: Esercizio8_eafp.py
#AUTORE: Beatrice Zavattin 
#DATA: 01/08/2026
#VERSIONE: 1.0
#DESCRIZIONE: Un gioco dell'impiccato in Python scritto interamente in stile EAFP: usa try/except (invece di if di controllo) per gestire lettura del file JSON, verifica 
#delle lettere indovinate/tentate e validazione della parola finale. Il giocatore ha 6 tentativi per indovinare la parola scelta a caso, lettera per lettera o tutta intera, 
#con stato di gioco mostrato a ogni turno tramite funzioni separate per caricamento, visualizzazione e controllo completamento.

import json
import random # generare scelte casuali

FILE_PAROLE = "parole.json"
TENTATIVI_MAX = 6


def carica_parola(percorso):
    """Carica la lista di parole e ne sceglie una a caso"""

    # --- EAFP: lettura del file ---
    try:
        with open(percorso, "r") as file_parole:
            dati = json.load(file_parole) # legge il contenuto del file e lo converte in una struttura dati Python (dizionario)
    except FileNotFoundError:
        print(f"Errore: il file '{percorso}' non esiste.")
        return None

    # --- EAFP: accesso alla chiave "parole" e scelta della parola casuale ---
    try: 
        lista_parole = dati["parole"] # accedere alla chiave
        generatore = random.Random() # crea un'istanza indipendente del generatore di numeri casuali
        indici = list(range(len(lista_parole)))
        generatore.shuffle(indici) # mescola casualmente
        parola = lista_parole[indici[0]] # recupera la parola corrispondente
    except KeyError:
        print("Errore: il file JSON non contiene la chiave 'parole'.")
        return None
    except IndexError:
        print("Errore: la lista delle parole è vuota.")
        return None

    return parola


def mostra_stato(parola, lettere_indovinate, lettere_tentate, tentativi_rimasti):
    """Stato corrente della partita"""

    mascherata = '' # inizializza una stringa vuota che conterrà la rappresentazione della parola con le lettere indovinate mostrate e le altre nascoste
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
    """Controlla se tutte le lettere sono state indovinate."""
    completa = True
    for lettera in parola:
        try:
            lettere_indovinate[lettera]
        except KeyError:
            completa = False
    return completa


def gioca(parola):
    """Ciclo principale del gioco"""

    lettere_indovinate = {}
    lettere_tentate = {}
    tentativi_rimasti = TENTATIVI_MAX

    # dizionario che mappa ogni lettera della parola al numero di volte che compare
    lettere_della_parola = {}
    for lettera in parola:
        try:
            lettere_della_parola[lettera] += 1
        except KeyError: # chiave non esiste
            lettere_della_parola[lettera] = 1

    # Dizionario con un'unica chiave valida: la parola corretta stessa
    parola_valida = {parola: True}

    while tentativi_rimasti > 0:

        if parola_completata(parola, lettere_indovinate):
            print(f"\nHai indovinato! La parola era '{parola}'.")
            return

        mostra_stato(parola, lettere_indovinate, lettere_tentate, tentativi_rimasti)

        scelta = input("Inserisci una lettera o prova l'intera parola: ")

        if len(scelta) == 0: # invio senza scrivere nulla
            continue

        if len(scelta) == 1: # una lettera

            # --- la lettera è già stata tentata? ---
            try:
                lettere_tentate[scelta] # lettera tentata 
            except KeyError:
                lettere_tentate[scelta] = True

                # --- la lettera appartiene alla parola? ---
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
            # --- la parola inserita è quella corretta? ---
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
    parola = carica_parola(FILE_PAROLE) # si sceglie parola per il gioco in maniera casuale

    if parola is not None: 
        gioca(parola)
    else:
        print("Impossibile avviare il gioco a causa di un errore nel file.")


main()
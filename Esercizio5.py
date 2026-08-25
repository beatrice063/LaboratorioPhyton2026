#
# File: Otto_regine_completo.py
#
# Author: (basato su E.Romelli, D.Tavagnacco)
#
# Date: 2026/08/25
#
# Version: 1.0
#
# Description: Esercizio completo sul problema delle 8 regine con
#              approccio brute force + permutazioni casuali.
#              Unisce in un unico programma tutti i 7 punti dell'Esercizio 5:
#              PUNTO 1) 10 soluzioni e tempo medio
#              PUNTO 2) conteggio tentativi per ogni soluzione
#              PUNTO 3) soluzioni "uniche" (nessuna ripetuta)
#              PUNTO 4) conteggio delle ripetizioni tra le soluzioni trovate
#              PUNTO 5) generalizzazione a scacchiera NxN
#              PUNTO 6) lato N massimo risolvibile in meno di 15 secondi
#              PUNTO 7) soluzioni simmetriche per rotazione (90/180/270 gradi)
#

import random
import time


# --------------------------------------------------------------------
# FUNZIONI DI BASE
# Sono usate da TUTTI i punti dell'esercizio (1-7) per verificare
# se una permutazione è una soluzione valida.
# --------------------------------------------------------------------

def stessa_diagonale(x0, y0, x1, y1):
    '''Ritorna Vero se posizioni (x0, y0) e (x1, y1) sono sulla stessa "diagonale"
    '''
    dy = abs(y1 - y0)
    dx = abs(x1 - x0)
    return dx == dy


def incrocia_colonne(posizioni, col):
    '''Ritorna Vero se la colonna 'col', che indica la posizione della regina
      (col, posizioni[col]) incrocia la diagonale di qualcuna
      delle posizioni delle regine precedenti
    '''
    for c in range(col):
        if stessa_diagonale(c, posizioni[c], col, posizioni[col]):
            return True
    return False


def soluzione_ok(soluzione_posizioni):
    '''Controlla tutte le posizioni della possibile soluzione
       'soluzione_posizioni' per verificare se ognuna delle posizioni
       incrocia la diagonale di qualche altra posizione
    '''
    for col in range(1, len(soluzione_posizioni)):
        if incrocia_colonne(soluzione_posizioni, col):
            return False
    return True


# --------------------------------------------------------------------
# FUNZIONI DI ROTAZIONE (PUNTO 7)
# Trasformano una soluzione (lista-permutazione) nella soluzione
# ottenuta ruotando la scacchiera di 90, 180 o 270 gradi.
# --------------------------------------------------------------------

def ruota_90(soluzione):
    '''PUNTO 7: ruota di 90 gradi (in senso orario) la soluzione data,
       ritornando la nuova lista-permutazione
    '''
    n = len(soluzione)
    nuova_soluzione = list(range(n))
    for riga in range(n):
        colonna = soluzione[riga]
        nuova_soluzione[colonna] = n - 1 - riga
    return nuova_soluzione


def ruota_180(soluzione):
    '''PUNTO 7: ruota di 180 gradi la soluzione data,
       ritornando la nuova lista-permutazione
    '''
    n = len(soluzione)
    nuova_soluzione = list(range(n))
    for riga in range(n):
        colonna = soluzione[riga]
        nuova_soluzione[n - 1 - riga] = n - 1 - colonna
    return nuova_soluzione


def ruota_270(soluzione):
    '''PUNTO 7: ruota di 270 gradi (in senso orario) la soluzione data,
       ritornando la nuova lista-permutazione
    '''
    n = len(soluzione)
    nuova_soluzione = list(range(n))
    for riga in range(n):
        colonna = soluzione[riga]
        nuova_soluzione[n - 1 - colonna] = riga
    return nuova_soluzione


# --------------------------------------------------------------------
# PUNTO 1: 10 soluzioni con le permutazioni e calcolo del tempo medio
# --------------------------------------------------------------------
def punto1_dieci_soluzioni_tempo_medio(random_generator):
    '''PUNTO 1: trova 10 soluzioni con le permutazioni e calcola
       il tempo medio necessario a trovarne una
    '''
    print('=== Punto 1: 10 soluzioni e tempo medio ===')

    scacchiera = list(range(8))
    numero_soluzioni_richieste = 10
    solutions = 0
    tempo_totale = 0

    while solutions < numero_soluzioni_richieste:
        # PUNTO 1: inizio la misurazione del tempo per QUESTA soluzione
        start_time = time.time()

        trovata = False
        while not trovata:
            random_generator.shuffle(scacchiera)
            if soluzione_ok(scacchiera):
                trovata = True

        # PUNTO 1: calcolo il tempo impiegato e lo accumulo per la media finale
        tempo_impiegato = time.time() - start_time
        tempo_totale += tempo_impiegato
        solutions += 1
        print(f'Found solution {scacchiera} in {tempo_impiegato} s.')

    # PUNTO 1: tempo medio = tempo totale diviso il numero di soluzioni trovate
    tempo_medio = tempo_totale / numero_soluzioni_richieste
    print(f'Tempo totale: {tempo_totale} s.')
    print(f'Tempo medio per trovare una soluzione: {tempo_medio} s.')
    print()


# --------------------------------------------------------------------
# PUNTO 2: conteggio dei tentativi necessari per ogni soluzione
# --------------------------------------------------------------------
def punto2_conta_tentativi(random_generator):
    '''PUNTO 2: conta quanti tentativi servono per trovare ogni soluzione
    '''
    print('=== Punto 2: conteggio tentativi per soluzione ===')

    scacchiera = list(range(8))
    numero_soluzioni_richieste = 10
    solutions = 0

    while solutions < numero_soluzioni_richieste:
        # PUNTO 2: contatore dei tentativi (shuffle), azzerato ad ogni nuova ricerca
        tentativi = 0

        trovata = False
        while not trovata:
            random_generator.shuffle(scacchiera)
            tentativi += 1  # PUNTO 2: incremento un tentativo ad ogni shuffle
            if soluzione_ok(scacchiera):
                trovata = True

        solutions += 1
        print(f'Found solution {scacchiera} after {tentativi} tentativi.')
    print()


# --------------------------------------------------------------------
# PUNTO 3: trovare soluzioni "uniche" (nessuna ripetuta)
# --------------------------------------------------------------------
def punto3_soluzioni_uniche(random_generator):
    '''PUNTO 3: trova 10 soluzioni "uniche" (nessuna ripetuta)
       Ritorna la lista delle soluzioni uniche trovate (riusata al PUNTO 7)
    '''
    print('=== Punto 3: soluzioni uniche ===')

    scacchiera = list(range(8))
    numero_soluzioni_richieste = 10

    # PUNTO 3: qui salvo le soluzioni già trovate, per non ripeterle
    lista_soluzioni_uniche = []

    while len(lista_soluzioni_uniche) < numero_soluzioni_richieste:
        trovata = False
        while not trovata:
            random_generator.shuffle(scacchiera)
            if soluzione_ok(scacchiera):
                trovata = True

        # PUNTO 3: accetto la soluzione solo se non è già nella lista
        if scacchiera not in lista_soluzioni_uniche:
            lista_soluzioni_uniche.append(scacchiera[:])
            print(f'Found solution {scacchiera}')

    print()
    return lista_soluzioni_uniche


# --------------------------------------------------------------------
# PUNTO 4: contare quante volte si ripete ogni soluzione
# --------------------------------------------------------------------
def punto4_conta_ripetizioni(random_generator):
    '''PUNTO 4: conta quante volte si ripete ogni soluzione trovata
       su un numero elevato di tentativi
    '''
    print('=== Punto 4: conteggio ripetizioni ===')

    scacchiera = list(range(8))
    numero_soluzioni_richieste = 300  # alto apposta per vedere le ripetizioni

    # PUNTO 4: dizionario chiave/valore per contare le occorrenze
    # (chiave = tupla della soluzione, perché una lista non è hashable
    #  e non può essere usata come chiave di un dizionario)
    conteggio_soluzioni = dict()

    solutions = 0
    while solutions < numero_soluzioni_richieste:
        trovata = False
        while not trovata:
            random_generator.shuffle(scacchiera)
            if soluzione_ok(scacchiera):
                trovata = True

        # PUNTO 4: converto in tupla e aggiorno il conteggio
        chiave = tuple(scacchiera)
        if chiave in conteggio_soluzioni.keys():
            conteggio_soluzioni[chiave] += 1
        else:
            conteggio_soluzioni[chiave] = 1
        solutions += 1

    print(f'Soluzioni distinte trovate: {len(conteggio_soluzioni)} su {numero_soluzioni_richieste} tentativi validi')
    print('--- Soluzioni ripetute più di una volta ---')
    # PUNTO 4: stampo solo le soluzioni che si sono ripetute più di una volta
    for chiave in conteggio_soluzioni.keys():
        if conteggio_soluzioni[chiave] > 1:
            print(f'{list(chiave)}  ->  trovata {conteggio_soluzioni[chiave]} volte')
    print()


# --------------------------------------------------------------------
# PUNTO 5: generalizzazione del problema a una scacchiera NxN
# --------------------------------------------------------------------
def punto5_scacchiera_NxN(random_generator):
    '''PUNTO 5: generalizza la ricerca a una scacchiera NxN qualsiasi,
       chiedendo N all'utente
    '''
    print('=== Punto 5: scacchiera NxN ===')

    # PUNTO 5: N viene chiesto all'utente invece di essere fissato a 8;
    # le funzioni di base sono già generiche (usano len()), quindi
    # funzionano automaticamente per qualsiasi N
    n = int(input('Inserisci la dimensione N della scacchiera: '))
    scacchiera = list(range(n))

    tentativi = 0
    solutions = 0
    while solutions < 1:
        random_generator.shuffle(scacchiera)
        tentativi += 1
        if soluzione_ok(scacchiera):
            print(f'Found solution {scacchiera} after {tentativi} tentativi.')
            solutions += 1
    print()


# --------------------------------------------------------------------
# PUNTO 6: N massimo risolvibile entro 15 secondi
# --------------------------------------------------------------------
def punto6_n_massimo_15_secondi(random_generator):
    '''PUNTO 6: trova il lato N più grande risolvibile in meno di 15 secondi
    '''
    print('=== Punto 6: N massimo risolvibile in meno di 15s ===')

    limite_tempo = 15  # secondi
    n = 4              # con 2 e 3 non esistono soluzioni al problema
    n_massimo_riuscito = 0
    continua = True

    while continua:
        scacchiera = list(range(n))
        # PUNTO 6: parte il cronometro per il tentativo con questo N
        start_time = time.time()

        solutions = 0
        while solutions < 1:
            random_generator.shuffle(scacchiera)

            if soluzione_ok(scacchiera):
                tempo_impiegato = time.time() - start_time
                print(f'N = {n}: Found solution {scacchiera} in {tempo_impiegato} s.')
                solutions += 1
                # PUNTO 6: N riuscito entro il limite, salvo e provo il successivo
                n_massimo_riuscito = n
                n += 1

            # PUNTO 6: se supero i 15 secondi senza trovare nulla, mi fermo
            if time.time() - start_time >= limite_tempo:
                break

        if solutions == 0:
            print(f'N = {n}: nessuna soluzione trovata entro {limite_tempo} s. (fermato)')
            continua = False

    print(f'La scacchiera più grande risolta in meno di {limite_tempo} s ha lato N = {n_massimo_riuscito}')
    print()


# --------------------------------------------------------------------
# PUNTO 7: soluzioni simmetriche per rotazione (90, 180, 270 gradi)
# --------------------------------------------------------------------
def punto7_simmetrie_rotazione(lista_soluzioni_uniche):
    '''PUNTO 7: per le prime 5 soluzioni uniche trovate al PUNTO 3,
       calcola le soluzioni simmetriche per rotazione di 90, 180, 270 gradi
    '''
    print('=== Punto 7: simmetrie per rotazione (90/180/270 gradi) ===')

    numero_da_mostrare = 5
    for i in range(numero_da_mostrare):
        # PUNTO 7: riuso le soluzioni uniche già trovate al PUNTO 3
        soluzione = lista_soluzioni_uniche[i]

        # PUNTO 7: applico le tre funzioni di rotazione definite sopra
        s90 = ruota_90(soluzione)
        s180 = ruota_180(soluzione)
        s270 = ruota_270(soluzione)

        print(f'--- Soluzione {i + 1} ---')
        print(f'Originale (0 gradi): {soluzione}')
        print(f'Ruotata 90 gradi   : {s90}')
        print(f'Ruotata 180 gradi  : {s180}')
        print(f'Ruotata 270 gradi  : {s270}')
    print()


def main():
    # inizializzo un unico generatore di permutazioni casuali
    # usato in tutto il programma (per tutti i 7 punti)
    random_generator = random.Random()

    # --- PUNTO 1 ---
    punto1_dieci_soluzioni_tempo_medio(random_generator)

    # --- PUNTO 2 ---
    punto2_conta_tentativi(random_generator)

    # --- PUNTO 3 --- (la lista di soluzioni uniche serve anche al PUNTO 7)
    lista_soluzioni_uniche = punto3_soluzioni_uniche(random_generator)

    # --- PUNTO 4 ---
    punto4_conta_ripetizioni(random_generator)

    # --- PUNTO 5 ---
    punto5_scacchiera_NxN(random_generator)

    # --- PUNTO 6 ---
    punto6_n_massimo_15_secondi(random_generator)

    # --- PUNTO 7 --- (riusa le soluzioni trovate al PUNTO 3)
    punto7_simmetrie_rotazione(lista_soluzioni_uniche)


main()

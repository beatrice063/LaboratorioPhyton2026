
#NOME: Esercizio3
#AUTORE: Beatrice Zavattin
#DATA: 25/04/2026
#VERSIONE: 1.0
#DESCRIZIONE:Esercizio che gestisce una rubrica (dizionario annidato) tramite riga di comando: permette di stampare tutti 
#i contatti, ordinarli per età (crescente e decrescente), generare messaggi di auguri personalizzati (per tutti o per una 
#singola persona) e cercare valori corrispondenti a una chiave specifica. Tutte le funzionalità sono gestite tramite opzioni 
#argparse, richiamabili singolarmente o insieme in un unico comando.


import argparse

rubrica = {
    'Paolino Paperino': {'giorno': 9, 'mese': 'giugno', 'anno': 1934,
                          'età': 93, 'sesso': 'M', 'mail': 'paolino.paperin0@disney.org'},
    'Ron Weasley': {'giorno': 1, 'mese': 'marzo', 'anno': 1980,
                     'età': 46, 'sesso': 'M', 'mail': 'ron_weasley80@hogwards.uk'},
    'Ramona Flowers': {'giorno': 19, 'mese': 'ottobre', 'anno': 2004,
                        'età': 22, 'sesso': 'F', 'mail': 'ramona.fls@gmail.com'},
    'Madoka Ayukawa': {'giorno': 25, 'mese': 'maggio', 'anno': 1969,
                        'età': 57, 'sesso': 'F', 'mail': 'madoka_sax@asahi_net.jp'}
}

chiavi_valide = ['giorno', 'mese', 'anno', 'età', 'sesso', 'mail']


# ---------- PUNTO 1 ----------
def punto1(rubrica):
    """Stampa ogni persona con tutte le sue coppie chiave-valore."""
    for nome, dati in rubrica.items():
        riga = f"'{nome}'"
        for chiave, valore in dati.items():
            if type(valore) == str:
                riga += f", '{chiave}' '{valore}'"
            else:
                riga += f", '{chiave}' {valore}"
        print(riga)


# ---------- Supporto per punti 2 e 3 ----------
def costruisci_lista_ordinata(rubrica):
    """Restituisce una lista di tuple (età, nome) ordinata in modo crescente.
    Ordinamento manuale (selection sort): .sort() non è spiegato in dettaglio nella teoria."""
    lista_età_nomi = []
    for nome, dati in rubrica.items():
        lista_età_nomi.append((dati['età'], nome))

    n = len(lista_età_nomi)
    for i in range(n):
        indice_minimo = i
        for j in range(i + 1, n):
            if lista_età_nomi[j][0] < lista_età_nomi[indice_minimo][0]:
                indice_minimo = j
        lista_età_nomi[i], lista_età_nomi[indice_minimo] = lista_età_nomi[indice_minimo], lista_età_nomi[i]

    return lista_età_nomi


# ---------- PUNTO 2 ----------
def punto2(rubrica):
    lista_ordinata = costruisci_lista_ordinata(rubrica)
    lista_età = [coppia[0] for coppia in lista_ordinata]
    lista_nomi = [coppia[1] for coppia in lista_ordinata]
    print("Età in ordine crescente:", lista_età)
    print("Nomi in ordine crescente di età:", lista_nomi)


# ---------- PUNTO 3 ----------
def punto3(rubrica):
    lista_ordinata = costruisci_lista_ordinata(rubrica)

    lista_invertita = []
    indice = len(lista_ordinata) - 1
    while indice >= 0:
        lista_invertita.append(lista_ordinata[indice])
        indice -= 1

    lista_età_inv = [coppia[0] for coppia in lista_invertita]
    lista_nomi_inv = [coppia[1] for coppia in lista_invertita]
    print("Età in ordine decrescente:", lista_età_inv)
    print("Nomi in ordine decrescente di età:", lista_nomi_inv)


# ---------- PUNTO 4 e PUNTO 6 (uniti: nome_filtro opzionale) ----------
def punto4(rubrica, nome_filtro=None):
    """Stampa il messaggio di auguri.
    Se nome_filtro è indicato, lo stampa solo per quella persona (punto 6)."""
    trovato = False
    for nome, dati in rubrica.items():
        if nome_filtro is not None and nome != nome_filtro:
            continue
        trovato = True

        if dati['sesso'] == 'M':
            o_a = 'o'
        else:
            o_a = 'a'

        messaggio = (f"Car{o_a} {nome},\n"
                     f"sei nat{o_a} il {dati['giorno']} di {dati['mese']} del {dati['anno']} "
                     f"e quindi a breve compirai {dati['età']} anni.\n"
                     f"Ti manderemo gli auguri a {dati['mail']}")
        print(messaggio)
        print()

    if nome_filtro is not None and not trovato:
        print(f"Nome '{nome_filtro}' non presente in rubrica.")


# ---------- PUNTO 5 ----------
def punto5(rubrica, chiave):
    """Stampa, per ogni persona, il valore corrispondente alla chiave data."""
    if chiave in chiavi_valide:
        for nome, dati in rubrica.items():
            print(f"{nome}: {dati[chiave]}")
    else:
        print(f"Chiave '{chiave}' non valida. Chiavi disponibili: {chiavi_valide}")


# ---------- PUNTO 7: argparse con tutte le opzioni ----------
parser = argparse.ArgumentParser(
    prog="esercizio_3.py",
    description="Gestione rubrica: eseguire una o più operazioni sulla rubrica")

parser.add_argument('--stampa_tutto', action='store_true',
                     help="Punto 1: stampa tutto il contenuto della rubrica")
parser.add_argument('--lista_ordinata', action='store_true',
                     help="Punto 2: mostra età e nomi ordinati in modo crescente")
parser.add_argument('--lista_invertita', action='store_true',
                     help="Punto 3: mostra età e nomi ordinati in modo decrescente")
parser.add_argument('--auguri', action='store_true',
                     help="Punto 4: stampa il messaggio di auguri (per tutti, o solo per --nome se indicato)")
parser.add_argument('--cerca_chiave',
                     help=f"Punto 5: mostra i valori di una chiave data {chiavi_valide}")
parser.add_argument('-n', '--nome',
                     help="Punto 6: nome e cognome della persona (es. 'Madoka Ayukawa'); "
                          "usato da solo o insieme a --auguri filtra il messaggio per quella persona")

args = parser.parse_args()

if args.stampa_tutto:
    punto1(rubrica)

if args.lista_ordinata:
    punto2(rubrica)

if args.lista_invertita:
    punto3(rubrica)

# --auguri da solo -> punto 4 completo
# --auguri --nome "X" oppure solo --nome "X" -> punto 6 (filtrato)
if args.auguri or args.nome:
    punto4(rubrica, nome_filtro=args.nome)

if args.cerca_chiave:
    punto5(rubrica, args.cerca_chiave)

# Se nessuna opzione è stata fornita, avviso l'utente
if not any([args.stampa_tutto, args.lista_ordinata, args.lista_invertita,
            args.auguri, args.cerca_chiave, args.nome]):
    print("Nessuna opzione fornita. Usa --help per vedere le opzioni disponibili.")

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


# ---------- Punto 1 ----------
def stampa_dizionario():
    for nome in rubrica:
        info = rubrica[nome]
        riga = f"'{nome}'"
        for campo in info:
            valore = info[campo]
            if type(valore) == str:
                riga += f", '{campo}' '{valore}'"
            else:
                riga += f", '{campo}' {valore}"
        print(riga)


# ---------- Funzione di supporto per punti 2 e 3 (selection sort manuale) ----------
def ordina_per_eta():
    nomi_lista = []
    eta_lista = []
    for nome in rubrica:
        nomi_lista.append(nome)
        eta_lista.append(rubrica[nome]['età'])

    n = len(eta_lista)
    for i in range(n):
        indice_minimo = i
        for j in range(i + 1, n):
            if eta_lista[j] < eta_lista[indice_minimo]:
                indice_minimo = j
        eta_lista[i], eta_lista[indice_minimo] = eta_lista[indice_minimo], eta_lista[i]
        nomi_lista[i], nomi_lista[indice_minimo] = nomi_lista[indice_minimo], nomi_lista[i]

    return nomi_lista, eta_lista


# ---------- Punto 2 ----------
def lista_ordinata():
    nomi_lista, eta_lista = ordina_per_eta()
    print("Età ordinate:", eta_lista)
    print("Nomi in ordine crescente di età:")
    for nome in nomi_lista:
        print(nome)


# ---------- Punto 3 ----------
def lista_invertita():
    nomi_lista, eta_lista = ordina_per_eta()
    n = len(eta_lista)
    eta_lista_invertita = []
    for i in range(n - 1, -1, -1):
        eta_lista_invertita.append(eta_lista[i])
    print("Età invertite:", eta_lista_invertita)


# ---------- Funzione di supporto per punti 4 e 6 ----------
def messaggio_auguri(nome):
    info = rubrica[nome]
    if info['sesso'] == 'M':
        des = 'o'
    else:
        des = 'a'
    messaggio = f"""Car{des} {nome},
sei nat{des} il {info['giorno']} di {info['mese']} del {info['anno']} e quindi a breve compirai {info['età']} anni.
Ti manderemo gli auguri a {info['mail']}"""
    print(messaggio)
    print()


# ---------- Punto 4 ----------
def auguri_a_tutti():
    for nome in rubrica:
        messaggio_auguri(nome)


# ---------- Punto 5 ----------
def cerca_per_chiave(chiave):
    for nome in rubrica:
        info = rubrica[nome]
        print(info[chiave])


# ---------- Configurazione argparse (punti 5, 6, 7) ----------
parser = argparse.ArgumentParser(
    prog='esercizio_finale.py',
    description='Gestione rubrica: stampa, ordinamento, auguri, ricerca per chiave'
)
parser.add_argument('--stampa_dizionario', action='store_true',
                     help='Esegue il punto 1: stampa il contenuto della rubrica')
parser.add_argument('--lista_ordinata', action='store_true',
                     help='Esegue il punto 2: età e nomi in ordine crescente di età')
parser.add_argument('--lista_invertita', action='store_true',
                     help='Esegue il punto 3: età in ordine decrescente')
parser.add_argument('--auguri', action='store_true',
                     help='Esegue il punto 4: messaggio di auguri per tutti')
parser.add_argument('-k', '--chiave',
                     help='Esegue il punto 5: mostra i valori corrispondenti alla chiave indicata')
parser.add_argument('-n', '--nome',
                     help='Esegue il punto 6: messaggio di auguri solo per il nome indicato')
args = parser.parse_args()

if args.stampa_dizionario:
    stampa_dizionario()

if args.lista_ordinata:
    lista_ordinata()

if args.lista_invertita:
    lista_invertita()

if args.auguri:
    auguri_a_tutti()

if args.chiave:
    cerca_per_chiave(args.chiave)

if args.nome:
    messaggio_auguri(args.nome)
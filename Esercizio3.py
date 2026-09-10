
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
    'Paolino Paperino': {'giorno': 9, 'mese': 'giugno', 'anno': 1934, 'età': 93, 'sesso': 'M', 'mail': 'paolino.paperin0@disney.org'},
    'Ron Weasley': {'giorno': 1, 'mese': 'marzo', 'anno': 1980, 'età': 46, 'sesso': 'M', 'mail': 'ron_weasley80@hogwards.uk'},
    'Ramona Flowers': {'giorno': 19, 'mese': 'ottobre', 'anno': 2004, 'età': 22, 'sesso': 'F', 'mail': 'ramona.fls@gmail.com'},
    'Madoka Ayukawa': {'giorno': 25, 'mese': 'maggio', 'anno': 1969, 'età': 57, 'sesso': 'F', 'mail': 'madoka_sax@asahi_net.jp'}
}


def punto1():
    for nome in rubrica:
        riga = f"'{nome}'"
        for campo in rubrica[nome]:
            valore = rubrica[nome][campo]
            if type(valore) == str:
                riga += f", '{campo}' '{valore}'"
            else:
                riga += f", '{campo}' {valore}"
        print(riga)


def punto2():
    nomi = []
    eta = []
    for nome in rubrica:
        nomi.append(nome)
        eta.append(rubrica[nome]['età'])
    for i in range(len(eta)):
        minimo = i
        for j in range(i + 1, len(eta)):
            if eta[j] < eta[minimo]:
                minimo = j
        eta[i], eta[minimo] = eta[minimo], eta[i]
        nomi[i], nomi[minimo] = nomi[minimo], nomi[i]
    print("Età ordinate:", eta)
    for nome in nomi:
        print(nome)


def punto3():
    nomi = []
    eta = []
    for nome in rubrica:
        nomi.append(nome)
        eta.append(rubrica[nome]['età'])
    for i in range(len(eta)):
        minimo = i
        for j in range(i + 1, len(eta)):
            if eta[j] < eta[minimo]:
                minimo = j
        eta[i], eta[minimo] = eta[minimo], eta[i]
    invertita = []
    for i in range(len(eta) - 1, -1, -1):
        invertita.append(eta[i])
    print("Età invertite:", invertita)


def auguri(nome):
    info = rubrica[nome]
    if info['sesso'] == 'M':
        des = 'o'
    else:
        des = 'a'
    print(f"Car{des} {nome},")
    print(f"sei nat{des} il {info['giorno']} di {info['mese']} del {info['anno']} e quindi a breve compirai {info['età']} anni.")
    print(f"Ti manderemo gli auguri a {info['mail']}")
    print()


def punto4():
    for nome in rubrica:
        auguri(nome)


def punto5(chiave):
    for nome in rubrica:
        print(rubrica[nome][chiave])


parser = argparse.ArgumentParser()
parser.add_argument('--stampa', action='store_true')
parser.add_argument('--ordina', action='store_true')
parser.add_argument('--inverti', action='store_true')
parser.add_argument('--auguri', action='store_true')
parser.add_argument('-k', '--chiave')
parser.add_argument('-n', '--nome')
args = parser.parse_args()

if args.stampa:
    punto1()

if args.ordina:
    punto2()

if args.inverti:
    punto3()

if args.auguri:
    punto4()

if args.chiave:
    punto5(args.chiave)

if args.nome:
    auguri(args.nome)
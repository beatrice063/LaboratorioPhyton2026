
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
    'Paolino Paperino': {'giorno': 9, 'mese': 'giugno', 'anno': 1934, 'età': 93,
                          'sesso': 'M', 'mail': 'paolino.paperin0@disney.org'},
    'Ron Weasley': {'giorno': 1, 'mese': 'marzo', 'anno': 1980, 'età': 46,
                     'sesso': 'M', 'mail': 'ron_weasley80@hogwards.uk'},
    'Ramona Flowers': {'giorno': 19, 'mese': 'ottobre', 'anno': 2004, 'età': 22,
                        'sesso': 'F', 'mail': 'ramona.fls@gmail.com'},
    'Madoka Ayukawa': {'giorno': 25, 'mese': 'maggio', 'anno': 1969, 'età': 57,
                        'sesso': 'F', 'mail': 'madoka_sax@asahi_net.jp'}
}


# ---------- PUNTO 1 ----------
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


# ---------- PUNTO 2 ----------
# Restituisce le due liste ordinate (nomi, eta) invece di stamparle soltanto,
# così possiamo riusarle anche nel punto 3 senza ricalcolare l'ordinamento.
def ordina_per_eta():
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

    return nomi, eta


def punto2():
    nomi, eta = ordina_per_eta()
    print("Età ordinate:", eta)
    for nome in nomi:
        print(nome)


# ---------- PUNTO 3 ----------
def punto3():
    nomi, eta = ordina_per_eta()
    # invertiamo l'ordine "a mano" scorrendo dall'ultimo indice al primo
    # (evitiamo lo slicing con step [::-1], non trattato a lezione:
    # usiamo solo range() e indicizzazione, visti in Lezione 2 e 4)
    n = len(eta)
    eta_inv = []
    nomi_inv = []
    for i in range(n):
        eta_inv.append(eta[n - 1 - i])
        nomi_inv.append(nomi[n - 1 - i])
    print("Età in ordine decrescente:", eta_inv)
    for nome in nomi_inv:
        print(nome)


# ---------- PUNTO 4 ----------
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


# ---------- PUNTO 5 ----------
def punto5(chiave):
    # validazione manuale della chiave con 'in' su una lista
    # (evitiamo choices=[...] di argparse, non trattato a lezione;
    # lo stesso pattern "if x in lista" si trova nell'esempio EAFP/LBYL
    # della Lezione 12: "if c in dizionario.keys():")
    chiavi_valide = ['giorno', 'mese', 'anno', 'età', 'sesso', 'mail']
    if chiave not in chiavi_valide:
        print(f"'{chiave}' non è una chiave valida.")
        return
    for nome in rubrica:
        print(f"'{nome}': {rubrica[nome][chiave]}")


# ---------- MAIN CON ARGPARSE ----------
def main():
    parser = argparse.ArgumentParser(description="Esercizio rubrica")

    # punto 5: chiave generica passata come opzione
    # (niente choices=[...]: non è trattato a lezione, la validazione
    # è fatta "a mano" dentro punto5())
    parser.add_argument('--chiave',
                         help="Mostra il valore di questa chiave per tutti i membri della rubrica (punto 5)")

    # punto 6: nome singolo per gli auguri
    # (niente type=str: senza indicazioni argparse tratta comunque
    # l'argomento come stringa di default)
    parser.add_argument('--nome',
                         help="Mostra il messaggio di auguri solo per il nome indicato (punto 6)")

    # punto 7: opzioni per eseguire i singoli punti dell'esercizio
    parser.add_argument('--stampa_dizionario', action='store_true', help="Esegue il punto 1")
    parser.add_argument('--lista_ordinata', action='store_true', help="Esegue il punto 2")
    parser.add_argument('--lista_invertita', action='store_true', help="Esegue il punto 3")
    parser.add_argument('--auguri', action='store_true', help="Esegue il punto 4 (per tutti)")

    args = parser.parse_args()

    if args.stampa_dizionario:
        punto1()

    if args.lista_ordinata:
        punto2()

    if args.lista_invertita:
        punto3()

    if args.auguri:
        punto4()

    if args.chiave:
        punto5(args.chiave)

    if args.nome:
        if args.nome in rubrica:
            auguri(args.nome)
        else:
            print(f"'{args.nome}' non è presente in rubrica.")


if __name__ == '__main__':
    main()
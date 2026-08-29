"""
NOME: lista_spesa.py
DESCRIZIONE: Gestionale semplice di una lista della spesa.
             La lista e' rappresentata come una lista di dizionari,
             ognuno con "nome" e "quantita".
             Il salvataggio avviene su un file di testo semplice
             (una riga per prodotto, formato: nome;quantita),
             NON in formato JSON.
"""

NOME_FILE = "lista_spesa.txt"


def aggiungi_prodotto(lista, nome, quantita):
    """Aggiunge un prodotto alla lista (dict con nome e quantita)."""
    prodotto = {"nome": nome, "quantita": quantita}
    lista.append(prodotto)
    print(f"Aggiunto: {quantita} x {nome}")


def rimuovi_prodotto(lista, nome):
    """Rimuove il primo prodotto con quel nome dalla lista."""
    for prodotto in lista:
        if prodotto["nome"] == nome:
            lista.remove(prodotto)
            print(f"Rimosso: {nome}")
            return
    print(f"Prodotto '{nome}' non trovato nella lista.")


def stampa_lista(lista):
    """Stampa a schermo tutti i prodotti della lista."""
    if len(lista) == 0:
        print("La lista della spesa e' vuota.")
        return
    print("\n--- LISTA DELLA SPESA ---")
    for prodotto in lista:
        print(f"- {prodotto['quantita']} x {prodotto['nome']}")
    print("-------------------------\n")


def salva_su_file(lista, nome_file):
    """Salva la lista su un file di testo, una riga per prodotto."""
    with open(nome_file, "w") as file_out:
        for prodotto in lista:
            file_out.write(f"{prodotto['nome']};{prodotto['quantita']}\n")
    print(f"Lista salvata su '{nome_file}'.")


def carica_da_file(nome_file):
    """Carica la lista da un file di testo, se esiste."""
    lista = []
    try:
        with open(nome_file, "r") as file_in:
            for riga in file_in:
                riga = riga.strip()
                if len(riga) == 0:
                    continue
                nome, quantita = riga.split(";")
                lista.append({"nome": nome, "quantita": quantita})
        print(f"Lista caricata da '{nome_file}'.")
    except FileNotFoundError:
        print("Nessun file precedente trovato: si parte con una lista vuota.")
    return lista


def mostra_menu():
    """Stampa il menu delle operazioni disponibili."""
    print("Cosa vuoi fare?")
    print("1 - Aggiungi prodotto")
    print("2 - Rimuovi prodotto")
    print("3 - Mostra lista")
    print("4 - Salva ed esci")


def main():
    lista_spesa = carica_da_file(NOME_FILE)

    while True:
        mostra_menu()
        scelta = input("Scelta: ")

        if scelta == "1":
            nome = input("Nome prodotto: ")
            quantita = input("Quantita': ")
            aggiungi_prodotto(lista_spesa, nome, quantita)

        elif scelta == "2":
            nome = input("Nome prodotto da rimuovere: ")
            rimuovi_prodotto(lista_spesa, nome)

        elif scelta == "3":
            stampa_lista(lista_spesa)

        elif scelta == "4":
            salva_su_file(lista_spesa, NOME_FILE)
            print("Alla prossima spesa!")
            break

        else:
            print("Scelta non valida, riprova.\n")


if __name__ == "__main__":
    main()
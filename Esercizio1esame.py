
#NOME: Esercizio1esame.py
#AUTORE: Zavattin Beatrice
#VERSIONE: 1.0
#DATA:
#DESCRIZIONE:



def is_pari(n):
    """Restituisce True se n è pari, False altrimenti."""
    return n % 2 == 0


def genera_numero():
    """Chiede un numero intero positivo finché l'input non è valido."""
    numero = int(input("Inserisci un numero intero positivo: "))
    while numero <= 0:
        print("Numero non valido: deve essere positivo. Riprova.")
        numero = int(input("Inserisci un numero intero positivo: "))
    return numero


def genera_sequenza(numero):
    """Genera la lista della sequenza."""
    lista = [numero]
    while numero != 1 and len(lista) <= 100:
        if is_pari(numero):
            numero = numero // 2
        else:
            numero = numero * 3 + 1
        lista.append(numero)
    return lista


def analizza_sequenza(lista):
    """Restituisce massimo, lunghezza e somma della sequenza."""
    massimo = lista[0]
    lunghezza = len(lista)
    somma = 0
    for numero in lista:
        somma = somma + numero
        if numero > massimo:
            massimo = numero
    return massimo, lunghezza, somma


def ricerca(lista):
    """Stampa i numeri della lista divisibili per 5."""
    trovati = False
    for numero in lista:
        if numero % 5 == 0:
            print(numero)
            trovati = True
    if not trovati:
        print("Nessun numero divisibile per 5 in questa sequenza.")


def main():
    quanti = int(input("Quanti numeri vuoi testare? "))

    numero_migliore = None
    lunghezza_massima = 0
    contatore = 0

    while contatore < quanti:
        print(f"\n--- Numero {contatore + 1} di {quanti} ---")
        numero = genera_numero()
        sequenza = genera_sequenza(numero)
        massimo, lunghezza, somma = analizza_sequenza(sequenza)

        print(f"Sequenza generata: {sequenza}")
        print(f"Valore massimo raggiunto: {massimo}")
        print(f"Lunghezza sequenza: {lunghezza}")
        print(f"Somma totale: {somma}")
        print("Numeri divisibili per 5:")
        ricerca(sequenza)

        if lunghezza > lunghezza_massima:
            lunghezza_massima = lunghezza
            numero_migliore = numero

        contatore = contatore + 1

    print("\n--- RIEPILOGO FINALE ---")
    print(f"Il numero iniziale che ha generato la sequenza più lunga è {numero_migliore}")
    print(f"Lunghezza della sequenza più lunga: {lunghezza_massima}")


main()


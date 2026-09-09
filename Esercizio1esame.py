#NOME: Esercizio1esame.py
#AUTORE: Zavattin Beatrice
#VERSIONE: 1.0
#DATA:22/03/2026
#DESCRIZIONE:Il programma chiede all'utente quanti numeri interi positivi testare, e per ciascuno genera la sequenza, dimezzando i numeri 
#pari e applicando 3n+1 ai dispari, fino a raggiungere 1 o un limite di sicurezza di 100 passi. Per ogni sequenza calcola e stampa il valore 
#massimo raggiunto, la lunghezza, la somma totale e i numeri divisibili per 5. Al termine mostra un riepilogo indicando quale numero di 
#partenza ha prodotto la sequenza più lunga.



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
    # Dimostrazione della funzione is_pari (punto 1 dell'esercizio)
    numero_test = int(input("Inserisci un numero per testare is_pari: "))
    if is_pari(numero_test):
        print(f"{numero_test} è pari.")
    else:
        print(f"{numero_test} è dispari.")

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
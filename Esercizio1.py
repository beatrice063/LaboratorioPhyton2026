def is_pari(n):
    """Ritorna vero se "n" è pari, se no ritorna falso """

    risultato = False

    if n%2 == 0 :
        risultato = True


    return risultato

#####

main():
    numero = int( input ('Dammi un numero:') )

    #print(type(numero))

    result = is_pari(numero)

    print(result)

print(result)


def intero_positivo(n):
    while True:
        n = int(input("Immetti un numero intero positivo: "))
        if n <= 0:
            print("Inserimento non valido")
            n = int(input("Immetti un numero intero positivo: "))
        yield n
        









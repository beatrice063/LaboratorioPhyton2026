def is_pari(n):
    """Ritorna vero se "n" è pari, se no ritorna falso """

    risultato = False

    if n % 2 == 0 :
        risultato = True


    return risultato

#####

main():
    numero = int( input ('Dammi un numero:') )

    #print(type(numero))

    result = is_pari(numero)

    print(result)

print(result)



def intero_positivo():
    while True:
        n = int(input("Immetti un numero intero positivo: "))
        if n <= 0:
            print("Inserimento non valido")
            n = int(input("Immetti un numero intero positivo: "))
        yield n

#####

a = intero_positivo()
print(next(g))



def sequenza(n):
    lista = []
    while n != 1 and len(lista) <= 100:
        lista.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = (n * 3) + 1

     lista.append(n)
     return lista

#####



def analizza_sequenza(lista):
    massimo = lista[0]
    somma = 0
    lunghezza = 0

    for numero in lista:
        if numero > massimo:
            massimo = numero
        somma = somma +numero
        lunghezza = lunghezza + 1 
    return massimo, lunghezza, somma 

#####

 









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






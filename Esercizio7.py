def tabellina(n):
    """Generatore infinito: produce i multipli di n (0, n, 2n, 3n, ...)."""
    i = 0
    while True:
        yield i * n
        i += 1


# --- Programma principale ---

print("Benvenuto nel gioco delle tabelline!")

# Chiediamo il numero della tabellina, gestendo eventuali errori di input
while True:
    scelta = input("Con quale numero vuoi giocare alla tabellina? ")
    try:
        numero = int(scelta)
        break
    except ValueError:
        print("Devi inserire un numero intero valido. Riprova.")

gen = tabellina(numero)
moltiplicatore = 0
punteggio = 0
gioco_attivo = True

print("Digita 'ESCI' in qualsiasi momento per terminare il gioco.\n")

while gioco_attivo:
    valore_corretto = next(gen)
    domanda_moltiplicatore = moltiplicatore
    risposta_valida = False

    while not risposta_valida:
        risposta = input(f"Quanto fa {numero} x {domanda_moltiplicatore}? ")

        if risposta.upper() == 'ESCI':
            print(f"\nGrazie per aver giocato! Punteggio finale: {punteggio}/{moltiplicatore}")
            gioco_attivo = False
            break

        try:
            risposta_numero = int(risposta)
            risposta_valida = True
        except ValueError:
            try:
                float(risposta)
                print("Sono ammessi solo numeri interi, niente virgole o decimali! Riprova.")
            except ValueError:
                print("Input non valido: inserisci un numero intero (oppure 'ESCI' per terminare). Riprova.")

    if not gioco_attivo:
        break

    if risposta_numero == valore_corretto:
        print("Corretto!\n")
        punteggio += 1
    else:
        print(f"Sbagliato! La risposta corretta era {valore_corretto}.\n")

    moltiplicatore += 1

#NOME: Esercizio2
#AUTORE: Beatrice Zavattin
#DATA:01/04/2026
#VERSIONE: 1.0 
#DESCRIOZIONE:Esercizio di analisi e manipolazione testuale su un estratto poetico: conta righe/parole/caratteri. 
#Effettua sostituzioni e trasformazioni (maiuscole, inversioni), trova parole comuni tra strofe e costruisce dizionari di frequenza.
#Applica stringhe, liste, set, dizionari e funzioni usando solo tecniche di base. 




testo = '''
Day after day, day after day,
We stuck, nor breath nor motion;
As idle as a painted ship
Upon a painted ocean.

Water, water, every where,
And all the boards did shrink;
Water, water, every where,
Nor any drop to drink.

The very deep did rot: O Christ!
That ever this should be!
Yea, slimy things did crawl with legs
Upon the slimy sea.

About, about, in reel and rout
The death-fires danced at night;
The water, like a witch's oils,
Burnt green, and blue and white.
'''

# Caratteri di punteggiatura da "pulire" ai bordi delle parole
punteggiatura = ",.;:!?'\""

# Caratteri considerati alfanumerici (niente digitazione automatica: li elenco a mano)
lettere_valide = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'


#Definisco una funzione che toglie la punteggiatura solo ai bordi di una parola
#Il primo while sposta inizio in avanti finché il carattere in quella posizione è punteggiatura
#Il secondo while sposta fine all'indietro finché l'ultimo carattere è punteggiatura
#ultima str restituisce solo la parte "pulita", usando lo slicing.
def pulisci_parola(parola):
    """Toglie punteggiatura solo a inizio/fine parola, non nel mezzo."""
    inizio = 0
    fine = len(parola)
    while inizio < fine and parola[inizio] in punteggiatura: 
        inizio += 1
    while fine > inizio and parola[fine - 1] in punteggiatura:
        fine -= 1
    return parola[inizio:fine]


# ---------- 1. Righe non vuote ----------
righe = testo.split('\n')
contatore_righe = 0
for riga in righe:
    if riga.strip() != '':
        contatore_righe += 1
print("1) Righe non vuote:", contatore_righe)

# ---------- 2. Numero di parole ----------
parole = testo.split()
print("2) Numero di parole:", len(parole))

# ---------- 3. Caratteri alfanumerici ----------
contatore_alfanumerici = 0
for carattere in testo:
    if carattere in lettere_valide:
        contatore_alfanumerici += 1
print("3) Caratteri alfanumerici:", contatore_alfanumerici)

# ---------- 4. Occorrenze di una lettera scelta dall'utente ----------
lettera = input("Inserisci una lettera da cercare: ")
contatore_lettera = 0
for carattere in testo:
    if carattere == lettera:
        contatore_lettera += 1
print(f"4) La lettera '{lettera}' compare", contatore_lettera, "volte")

# ---------- 5. Sostituzione di day/water/about con PYTHON ----------
righe5 = testo.split('\n')
righe5_nuove = []
for riga in righe5:
    parole_riga = riga.split()
    parole_nuove = []
    for parola in parole_riga:
        inizio = 0
        fine = len(parola)
        while inizio < fine and parola[inizio] in punteggiatura:
            inizio += 1
        while fine > inizio and parola[fine - 1] in punteggiatura:
            fine -= 1
        prefisso = parola[:inizio]
        nucleo = parola[inizio:fine]
        suffisso = parola[fine:]
        if nucleo.lower() == 'day' or nucleo.lower() == 'water' or nucleo.lower() == 'about':
            parola_nuova = prefisso + 'PYTHON' + suffisso
        else:
            parola_nuova = parola
        parole_nuove.append(parola_nuova)
    righe5_nuove.append(' '.join(parole_nuove))
testo5 = '\n'.join(righe5_nuove)
print("5) Testo con sostituzioni:")
print(testo5)

# ---------- 6. Parole in posizione dispari in maiuscolo ----------
righe6 = testo.split('\n')
posizione = 0
righe6_nuove = []
for riga in righe6:
    parole_riga = riga.split()
    parole_nuove = []
    for parola in parole_riga:
        posizione += 1
        if posizione % 2 != 0:      # posizione dispari (1, 3, 5, ...)
            parole_nuove.append(parola.upper())
        else:
            parole_nuove.append(parola)
    righe6_nuove.append(' '.join(parole_nuove))
testo6 = '\n'.join(righe6_nuove)
print("6) Testo con parole dispari maiuscole:")
print(testo6)

# ---------- 7. Testo con le righe invertite dal basso verso l'alto ----------
righe7 = testo.split('\n')
righe7_invertite = []
for i in range(len(righe7) - 1, -1, -1):     # range con step negativo
    righe7_invertite.append(righe7[i])
testo7 = '\n'.join(righe7_invertite)
print("7) Testo con righe invertite:")
print(testo7)

# ---------- 8. Secondo verso di ogni strofa a specchio ----------
def inverti_stringa(s):
    invertita = ''
    for i in range(len(s) - 1, -1, -1):
        invertita = invertita + s[i]
    return invertita

strofe = testo.split('\n\n')
strofe_nuove = []
for strofa in strofe:
    righe_strofa = strofa.split('\n')
    righe_pulite = []
    for r in righe_strofa:
        if r.strip() != '':
            righe_pulite.append(r)
    if len(righe_pulite) >= 2:
        righe_pulite[1] = inverti_stringa(righe_pulite[1])
    strofe_nuove.append('\n'.join(righe_pulite))
testo8 = '\n\n'.join(strofe_nuove)
print("8) Testo con secondo verso a specchio:")
print(testo8)

# ---------- 9. Parole comuni a tutte le strofe ----------
strofe9 = testo.split('\n\n')
insiemi_strofe = []
for strofa in strofe9:
    parole_strofa = strofa.split()
    insieme = set()
    for p in parole_strofa:
        nucleo = pulisci_parola(p).lower()
        if nucleo != '':
            insieme.add(nucleo)
    insiemi_strofe.append(insieme)

comuni = insiemi_strofe[0]
for i in range(1, len(insiemi_strofe)):
    comuni = comuni & insiemi_strofe[i]     # intersezione tra insiemi
print("9) Parole comuni a tutte le strofe:", comuni)

# ---------- 10. Lista univoca di parole ordinata per lunghezza ----------
tutte_parole = testo.split()
parole_pulite = set()
for p in tutte_parole:
    nucleo = pulisci_parola(p).lower()
    if nucleo != '':
        parole_pulite.add(nucleo)
lista_univoca = list(parole_pulite)

# ordinamento manuale "a bolle" (sort con key non è nella teoria)
n = len(lista_univoca)
for i in range(n):
    for j in range(n - i - 1):
        if len(lista_univoca[j]) > len(lista_univoca[j + 1]):
            lista_univoca[j], lista_univoca[j + 1] = lista_univoca[j + 1], lista_univoca[j]

print("10) Numero di parole uniche:", len(lista_univoca))
print(lista_univoca)

# ---------- 11. Dizionario carattere -> occorrenze (tutti i caratteri) ----------
dizionario_caratteri = {}
for carattere in testo:
    if carattere in dizionario_caratteri:
        dizionario_caratteri[carattere] += 1
    else:
        dizionario_caratteri[carattere] = 1
print("11) Dizionario di tutti i caratteri:")
print(dizionario_caratteri)

# ---------- 12. Dizionario carattere -> occorrenze (solo alfanumerici, no maiuscole) ----------
dizionario_alfanumerici = {}
for carattere in testo:
    carattere_min = carattere.lower()
    if carattere_min in lettere_valide.lower():
        if carattere_min in dizionario_alfanumerici:
            dizionario_alfanumerici[carattere_min] += 1
        else:
            dizionario_alfanumerici[carattere_min] = 1
print("12) Dizionario solo caratteri alfanumerici (case-insensitive):")
print(dizionario_alfanumerici)
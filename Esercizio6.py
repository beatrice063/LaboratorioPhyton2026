#NOME: Esercizio6
#AUTORE: Beatrice Zavattin
#DATA: 03/07/2026
#VERSIONE: 1.0
#DESCRIZIONE:Trasformare la rubrica dell'Esercizio 3 in una classe Rubrica con 5 metodi (APRI, AGGIUNGI, RIMUOVI, SALVA, STAMPA) e gestione 
#degli errori, poi usarla in un programma interattivo che chiede l'azione da eseguire finché non si digita "EXIT".


# Importa il modulo integrato di Python per gestire i file in formato JSON (JavaScript Object Notation)
import json


# 1. DEFINIZIONE DELLA CLASSE RUBRICA


# Definisce la classe "Rubrica", il modello (blueprint) per creare i nostri oggetti rubrica
class Rubrica:
    """Una classe per gestire una rubrica telefonica con i dati dei contatti"""

    # Il costruttore della classe. Inizializza l'oggetto quando viene creato.
    # Accetta un dizionario iniziale facoltativo (il cui valore predefinito è None).
    def __init__(self, dizionario_iniziale=None):
        """Inizializza la rubrica con un dizionario"""
        self.contatti = dizionario_iniziale

    @classmethod
    def apri_da_json(cls, nome_file):
        """Inizializza la rubrica leggendo da un file JSON"""
        with open(nome_file, 'r') as f:
            dati = json.load(f)
        return cls(dati)

    @classmethod
    def apri_da_txt(cls, nome_file):
        """Inizializza la rubrica leggendo da un file di testo.

        Formato: una riga per contatto, campi separati da virgola:
        nome,giorno,mese,anno,età,sesso,mail
        """
        dati = {}
        with open(nome_file, 'r') as f:
            for riga in f:
                riga = riga.strip()
                if len(riga) == 0:
                    continue
                nome, giorno, mese, anno, età, sesso, mail = riga.split(',')
                dati[nome] = {'giorno': int(giorno),
                              'mese': mese,
                              'anno': int(anno),
                              'età': int(età),
                              'sesso': sesso,
                              'mail': mail}
        return cls(dati)

    def aggiungi(self, nome, dati_contatto):
        """Aggiunge un elemento alla rubrica"""
        if self.contatti is None:
            print("Prima apri una rubrica")
            return
        self.contatti[nome] = dati_contatto

    def rimuovi(self, nome):
        """Rimuove un elemento dalla rubrica dato il nome"""
        if self.contatti is None or self.contatti == {}:
            print("La rubrica è vuota")
            return
        if nome not in self.contatti.keys():
            print(f"Il contatto {nome} non esiste in rubrica")
            return
        del self.contatti[nome]

    def stampa(self, nome):
        """Stampa tutte le informazioni di un contatto dato il nome"""
        if self.contatti is None or self.contatti == {}:
            print("La rubrica è vuota")
            return
        if nome not in self.contatti.keys():
            print(f"Il contatto {nome} non esiste in rubrica")
            return

        contatto = self.contatti[nome]

        if contatto['sesso'] == 'M':
            desinenza = 'o'
        else:
            desinenza = 'a'

        messaggio = f"""Car{desinenza} {nome},
sei nat{desinenza} il {contatto['giorno']} di {contatto['mese']} del {contatto['anno']} e quindi a breve compirai {contatto['età']} anni.
Ti manderemo gli auguri a {contatto['mail']}"""
        print(messaggio)

    def salva(self, nome_file):
        """Salva la rubrica su file JSON o TXT"""
        if self.contatti is None or self.contatti == {}:
            print("La rubrica è vuota")
            return

        parti_nome = nome_file.split('.')
        estensione = parti_nome[-1]

        if estensione == 'json':
            with open(nome_file, 'w') as f:
                json.dump(self.contatti, f)
        else:
            with open(nome_file, 'w') as f:
                for nome in self.contatti:
                    contatto = self.contatti[nome]
                    riga = f"{nome},{contatto['giorno']},{contatto['mese']},{contatto['anno']},{contatto['età']},{contatto['sesso']},{contatto['mail']}\n"
                    f.write(riga)


# 2. PROGRAMMA INTERATTIVO PRINCIPALE
dati_rubrica = {
  'Paolino Paperino': {'giorno': 9, 'mese': 'giugno', 'anno': 1934, 'età': 93, 'sesso': 'M', 'mail': 'paolino.paperin0@disney.org'},
  'Ron Weasley': {'giorno': 1, 'mese': 'marzo', 'anno': 1980, 'età': 46, 'sesso': 'M', 'mail': 'ron_weasley80@hogwards.uk'},
  'Ramona Flowers': {'giorno': 19, 'mese': 'ottobre', 'anno': 2004, 'età': 22, 'sesso': 'F', 'mail': 'ramona.fls@gmail.com'},
  'Madoka Ayukawa': {'giorno': 25, 'mese': 'maggio', 'anno': 1969, 'età': 57, 'sesso': 'F', 'mail': 'madoka_sax@asahi_net.jp'}
}

rubrica = Rubrica(None)

while True:
    azione = input("\nInserisci l'azione (APRI, AGGIUNGI, RIMUOVI, SALVA, STAMPA) o 'EXIT': ").strip().upper()

    if azione == "EXIT":
        print("Programma terminato.")
        break

    elif azione == "APRI":
        scelta = input("Vuoi caricare da file 'JSON', 'TXT' o usare i dati di 'DEFAULT'? ").strip().upper()
        if scelta == "DEFAULT":
            rubrica = Rubrica(dati_rubrica)
            print("Rubrica predefinita caricata correttamente.")
        elif scelta == "JSON":
            nome_file = input("Nome del file JSON (es. rubrica.json): ")
            rubrica = Rubrica.apri_da_json(nome_file)
            print("Rubrica aperta da file JSON.")
        elif scelta == "TXT":
            nome_file = input("Nome del file TXT (es. rubrica.txt): ")
            rubrica = Rubrica.apri_da_txt(nome_file)
            print("Rubrica aperta da file di testo.")
        else:
            print("Scelta di caricamento non valida.")

    elif azione == "AGGIUNGI":
        nome = input("Inserisci Nome e Cognome: ")
        giorno = int(input("Inserisci giorno di nascita: "))
        mese = input("Inserisci mese di nascita: ")
        anno = int(input("Inserisci anno di nascita: "))
        eta = int(input("Inserisci età: "))
        sesso = input("Inserisci sesso (M/F): ")
        mail = input("Inserisci indirizzo mail: ")

        nuovo_contatto = {
            'giorno': giorno,
            'mese': mese,
            'anno': anno,
            'età': eta,
            'sesso': sesso,
            'mail': mail
        }
        rubrica.aggiungi(nome, nuovo_contatto)

    elif azione == "RIMUOVI":
        nome = input("Inserisci il nome del contatto da rimuovere: ")
        rubrica.rimuovi(nome)

    elif azione == "SALVA":
        nome_file = input("Inserisci il nome del file su cui salvare (es. rubrica.json o rubrica.txt): ")
        rubrica.salva(nome_file)

    elif azione == "STAMPA":
        nome = input("Inserisci il nome del contatto da stampare: ")
        rubrica.stampa(nome)

    else:
        print("Operazione non esistente. Riprova.")
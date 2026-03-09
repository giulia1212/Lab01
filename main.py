import random


# LABORATORIO 1

# leggo da file una domanda per volta, poi la insersco nell'array della sua difficoltà
class Domanda:
    def __init__(self, testo: str, difficolta: int, rispostaCorretta: str, errata1: str, errata2: str, errata3: str ):
        self.testo = testo
        self.difficolta = difficolta
        self.rispostaCorretta = rispostaCorretta
        self.errata1 = errata1
        self.errata2 = errata2
        self.errata3 = errata3

# sono liste di istanze di classe Domanda
domande = []

with open('domande.txt', 'r', encoding='utf-8') as file:
    while True:
        domanda = []
        for i in range(7):
            riga = file.readline()
            if not riga:  # fine file
                break
            domanda.append(riga.strip())
        if not domanda:  # se non ha letto nulla → esci
            break
        difficolta = int(domanda[1])
        dom = Domanda(domanda[0], difficolta, domanda[2], domanda[3], domanda[4], domanda[5])
        domande.append(dom)

#def gioca():
print("Benvenuto!!")
errore = False
livello = 0
punteggio = 0
while errore == False:
    domande_tra_cui_scegliere = []
    risposte = []
    for d in domande:
        if(d.difficolta == livello):
            domande_tra_cui_scegliere.append(d)


    if len(domande_tra_cui_scegliere)==0:
        print("Hai finito il gioco!")
        print(f"Il tuo punteggio è {punteggio}")
        break

    domanda_casuale = random.choice(domande_tra_cui_scegliere)
    risposte.append(domanda_casuale.rispostaCorretta)
    risposte.append(domanda_casuale.errata1)
    risposte.append(domanda_casuale.errata2)
    risposte.append(domanda_casuale.errata3)
    random.shuffle(risposte)
    print(domanda_casuale.testo)
    for risposta in risposte:
        print(risposta)
    risposta_utente = input("Inserisci la tua risposta: ")
    if(risposta_utente == domanda_casuale.rispostaCorretta):
        print("Complimenti risposta esatta!")
        livello += 1
        punteggio += 1
    else:
        print("Mi dispiace risposta errata :( ")
        errore = True
        print(f"Il tuo punteggio è {punteggio}")

    domande_tra_cui_scegliere.clear()
    risposte.clear()

nickname = input("Inserisci il tuo nickname: ")

# dizionario dei punteggi
punteggi = {}
with open("punti.txt", "r") as file:
    for riga in file:
        parti = riga.strip().split()
        # riempie il dizionario
        if len(parti) == 2 and parti[1].isdigit():
            punteggi[parti[0]] = int(parti[1])

# Aggiorno o inserisco il punteggio
punteggi[nickname] = punteggio

def per_punteggio(item):
    # item è una tupla (nome, punti)
    return item[1]

# Ordino in ordine decrescente
lista_ordinata = sorted(punteggi.items(), key=per_punteggio,  reverse=True)

# Riscrivo il file
with open("punti.txt", "w") as file:
    for nome, punti in lista_ordinata:
        file.write(f"{nome} {punti}\n")




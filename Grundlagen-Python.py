# grundlagen python.py
import random
# <-- Kommentare

# Ausgabe von daten
print("Hello World")

# Variablen definieren (kann ohne Typ erfolgen)
heimat = "Erde"

# Mehrere Variablen werden mit , getrennt
print(heimat, "to World: " , "Hallo!")

# Eingabe / liest Text(!) von der Konsole ein
wer = input("Und wer bist du? ")

# und gibt den Text wieder aus
if (wer == "ich"):
    print("Hallo du")
else:
    print ("Hallo", wer)

lieblingszahl = input("Was ist deine Lieblingszahl? ")
print("Super, ich mag die Zahl " , lieblingszahl)
print("Aber die groessere Zahl", int(lieblingszahl)+10, " mag ich noch mehr!")

runden = input("Wie viele Runden sollen wir spielen? ")
runden = int(runden)

user = 0
Pc = 0
for i in range(0,runden):
    sieger = " "
    #zufallszahl erzeugen
    zufallszahl = random.randint(1,6)
    if (zufallszahl == 1 or zufallszahl == 3 or zufallszahl == 5):
        sieger = "ich"
        user = user + 1
    else:
        sieger = "Pc"
        Pc =  Pc + 1
    
    print("Runde " , (i + 1) , " von " , runden , ": Sieger: " , sieger , " <" , zufallszahl , ">")
if(user > Pc):
    print("Es hat <User> gewonnen ( mit " , user , " Siegen zu " , Pc , " )")
elif(user < Pc):
    print("Es hat <Pc> gewonnen ( mit " , Pc , " Siegen zu " , user , " )")
else:
    print("Unentschieden ( mit "  , user , " Siegen zu " , Pc , " )")
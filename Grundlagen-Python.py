# grundlagen python.py

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
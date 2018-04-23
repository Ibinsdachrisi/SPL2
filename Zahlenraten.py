# Zahlenraten
import random

maxbegi = input("Range: ")
rand = random.randint(1,int(maxbegi))
gewonnen = false
zw = 0
g = 0
i = 0
div = 0
max = maxbegi
letzte = max


while(gewonnen != true):
    i = i + 1


    
    if(rand < zw):
        g = 0
    elif(rand > zw):
        g = 1
    else:
        print("Pc gewonnen nach " , 1)
        break

    max2 = max

    if(g == 1):
        max =  max / 4 * 3
    elif(g == 0):
        max = max / 4 * 1
    else:
        print("Fehler")



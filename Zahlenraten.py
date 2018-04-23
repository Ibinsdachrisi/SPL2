# Zahlenraten
import random

maxbegi = input("Range: ")
maxbegi = int(maxbegi)

#rand = random.randint(1,int(maxbegi))
rand = 150

gewonnen = "false"
zw = 0
g = 0
i = 0
div = 0
max = maxbegi / 2
max = int(max)
letzte = max


while(gewonnen != "true"):
    i = i + 1
    if(i > 10):
        break

    
    if(rand < max):
        g = 0
    elif(rand > max):
        g = 1
    else:
        print("Pc gewonnen nach " , 1)
        break

    max2 = max

    if(g == 1):
        max =  int(max / 4 * 3)
        print(max)
    elif(g == 0):
        max = int( max / 4 * 2)
        print(max)
    else:
        print("Fehler")



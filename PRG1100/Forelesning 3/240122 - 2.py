liste=[5,3,1,2,4]

bytte=True
stoppMerke=1


while bytte==True:
    print("Starter på while-løkka")

    bytte=False

    for x in range (0,len(liste)-stoppMerke,1):
        print("Starter på for-løkka")
        if liste[x]>liste[x+1]:
            temp=liste[x]
            liste[x]=liste[x+1]
            liste[x+1]=temp
            bytte=True
            print("Resultat etter bytte nr.",x+1)
            print(liste)
    print("Slutt på for løkke")
    print()

    stoppMerke=stoppMerke+1

print("Slutt på while-løkka")
print("Den sorterte lista er:", liste)
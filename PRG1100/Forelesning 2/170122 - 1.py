liste=[5,3,1,2,4] 

for x in range (0,len(liste)-1,1):

    if liste[x]>liste[x+1]:
        temp=liste[x]
        liste[x]=liste[x+1]
        liste[x+1]=temp
        print("Resultat etter bytte nr.",x+1)
        print(liste)
        print()
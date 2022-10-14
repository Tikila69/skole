liste=[5,4,3,2,1]

for n in range (0,len(liste)-1,1):

    print("Da starter gjennomgang nr.", n+1)

    for x in range (0,len(liste)-1,1):

        if liste[x]>liste[x+1]:
            temp=liste[x]
            liste[x]=liste[x+1]
            liste[x+1]=temp
            print("Resultat etter bytte nr.",x+1)
            print(liste)
            print()

print("Den sorterte lista er:", liste)

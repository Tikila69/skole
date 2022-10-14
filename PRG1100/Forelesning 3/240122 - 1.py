#liste=[5,3,1,2,4,7,6]

liste=[]

skriveTall=True

while skriveTall==True:
    tall=int(input("Vennligst skriv inn neste tall i lista: "))
    liste+=[tall]
    fortsette=input("Ønsker du fylle inn flere tall i liste? (j/n): ")
    if  fortsette=="n":
        skriveTall=False

for n in range (0,len(liste)-1,1):

    print("Da starter gjennomgang nr.", n+1)

    for x in range (0,len(liste)-1,1):

        if liste[x]>liste[x+1]:
            temp=liste[x]
            liste[x]=liste[x+1]
            liste[x+1]=temp
            print("Kontrollere possesjon",x+1,"med possesjon",x+2)
            print("Resultat etter bytte nr.",x+1)
            print(liste)
            print()

print("Den sorterte lista er:", liste)

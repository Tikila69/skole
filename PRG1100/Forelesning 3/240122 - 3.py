liste=[5,3,1,2,4]

print("liste før sortering:",liste)
for i in range (1,len(liste),1):

    print("kort nr.",i+1,"med verdi",liste[i])

    j=i
    flyttes=0
    
    while j>0 and liste[j-1]>liste[j]:
        temp1=liste[j-1]
        liste[j-1]=liste[j]
        liste[j]=temp1
        j=j-1
        flyttes=flyttes+1
        print("Flyttes",flyttes,"gang(er) til venstre og resultat blir",liste)

print("Slutt på for-løkke og sortert liste blir",liste)
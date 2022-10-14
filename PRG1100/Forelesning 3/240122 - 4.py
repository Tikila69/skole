liste=[5,3,1,2,4]

print("liste før sortering:",liste)
for i in range (1,len(liste),1):
    print("Vi jobber med kort nr",i+1,)
    print("Det har verdi",liste[i])

    print('"kortet tas ut"')
    x=liste[i]
    j=i-1

    
    flyttet=0
    while j>=0 and liste[j]>x:
        liste[j+1]=liste[j]
        j=j-1
        flyttet=flyttet+1
    liste[j+1]=x
    print("Og",flyttet,'"kort" foran flyttes til høyre før "kortet" settes inn')
    print("Resultat så langt:",liste)
    print()
print("Slutt på for-løkke og sortert liste blir",liste)
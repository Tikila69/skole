#Åpne fil og definere lister
oppbevaringer=open('oppbevaring.txt','r')
liste=[]
listeSøk=[]

#Lese hele filen og skrive det til liste
linje=oppbevaringer.readline()
while linje!='':
    liste+=[linje.rstrip('\n')]
    linje=oppbevaringer.readline()
oppbevaringer.close()

#Be bruker om mobilnummer
mobilnr=input('Oppgi mobilnummer: ')

#Finne alle instanser med mobilnummer og print skriv dem over til liste
for x in range (0,len(liste),6):
    if liste[x]==mobilnr:
        listeSøk=[liste[x]]+[liste[x+1]]+[liste[x+2]]+[liste[x+3]]+[liste[x+4]]+[liste[x+5]]
    #Print liste
    print(listeSøk)
#Program for å lese 5 tall inn i en liste og finne det minste tallet

#talliste defiernes som en tom liste
talliste=[]

#Utskrift av listeinnhold før fylling
print('Lista til nå:',talliste)
print()

#FOR-løkke å lese 5 tall inn i lista talliste
for index in range (0,5,1):
    print('tall nr:',index+1)
    listeverdi=int(input('Oppgi tall: '))
    #Innlest listeverdi legges inn i lista
    talliste+=[listeverdi]
    #Utskrift av listeinnhold underveis/med fylling
    print('Lista til nå:',talliste)
    print()

#Utskrift av listeinnhold og listestørresle etter fylling
print('Hele lista er:',talliste,)
listeLengde=len(talliste)
print('Antall elementer i lista er:',listeLengde)
print()
print('Lista er ferdig fylt ut')
print()

#Oppgave til neste gang:
#Utvid programmet til å finne minste tallet og tallnr i lista

minsteTall=talliste[0]
tallnr=1

for index in range (1,5,1):
    if talliste[index]<minsteTall:
        minsteTall=talliste[index]
        tallnr=index+1

print('Det minste tallet i tabellen er:',minsteTall,'og har index nr:',tallnr)
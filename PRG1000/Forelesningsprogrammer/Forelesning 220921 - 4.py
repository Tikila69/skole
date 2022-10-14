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

#Oppgave til neste gang:
#Utvid programmet til å finne minste tallet og tallnr i lista

if talliste[0]<talliste[1]:
    minst=talliste[0]
    minstIndex=1
else:
    minst=talliste[1]
    minstIndex=2
if talliste[2]<minst:
    minst=talliste[2]
    minstIndex=3
if talliste[3]<minst:
    minst=talliste[3]
    minstIndex=4
if talliste[4]<minst:
    minst=talliste[4]
    minstIndex=5
print('Det minste tallet i tabellen er:',minst,'og har index nr:',minstIndex)
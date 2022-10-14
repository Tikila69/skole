#Oppgave 1
#Lag et program som leser inn fornavn i lista fornavn. Det skal leses inn minst ett fornavn og brukeren skal spørres om 
#det skal leses inn et nytt navn. Det skal leses inn nye fornavn så lenge brukeren svarer ‘Ja’.
#Når brukeren svarer ‘Nei’ skal programmet først skrive ut innholdet i lista og deretter innholdet i lista fra siste til 
#første oppgitte fornavn. Utskrift av reversert listeinnhold skal både kodes fra bunnen av (gjøres først) og ved bruk av 
#reverse-metoden (gjøres sist), se Gaddis s 402.

navn=str(input('Skriv inn første navn i listen: '))
print()
navnliste=[]
navnliste+=[navn]

fortsette1="Ja"
while fortsette1=="Ja":
    fortsette1=str(input('Ønsker du å skrive inn flere navn? '))
    print()
    if fortsette1=="Ja":
        fortsette2=True
        while fortsette2==True:
            navn=str(input('Skriv inn det neste navnet i listen: '))
            print()
            navnliste+=[navn]
            fortsette2=False

print('Listen så lang:',navnliste)
print()

navnlisteRev=[]
for n in range (len(navnliste)-1,-1,-1):
    navnRev=navnliste[n]
    
    navnlisteRev+=[navnRev]

print('Navnlisten reversert er:',navnlisteRev)
print()
navnliste.reverse()
print('Med bruk av reverse:',navnliste)
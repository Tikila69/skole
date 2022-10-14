#Et bilutleiefirma tilbyr følgende alternativer for dagsleie av leiebil:
#1. fastpris 750 kr
#2. fastpris 300 kr og 2 kr pr kjørt km
#3. fastpris 150 kr og 4 kr pr kjørt km

#Kunden må velge et av alternativene ved inngåelse av leiekontrakten.

#Lag et program som sammenligner de tre alternativene, tabell 0-500 km med steg på 50 km, 
#og for hver rad avgjør hvilket alternativt som er best for kunden.

#Definere variablene
fastpris1=750
fastpris2=300
fastpris3=150
kmPris1=2
kmPris2=4

#Sett opp løkken
for n in range (0,501,50):

#Beregne priser
    pris1=fastpris2+(n*kmPris1)
    pris2=fastpris3+(n*kmPris2)

#Sammenlign prisen
    if fastpris1<pris1 and fastpris1<pris2:
        print('For',n,'kilometer er alternativ 1 billigst')
    elif pris1<pris2 and pris1<fastpris1:
        print('For',n,'kilometer er alternativ 2 billigst')
    else:
        print('For',n,'kilometer er alternativ 3 billigst')
#Et bilutleiefirma tilbyr følgende alternativer for dagsleie av leiebil:
#1. fastpris 750 kr
#2. fastpris 300 kr og 2 kr pr kjørt km
#3. fastpris 150 kr og 4 kr pr kjørt km

#Kunden må velge et av alternativene ved inngåelse av leiekontrakten.
#Lag et program som sammenligner de tre alternativene ut fra antall km som inndata, og avgjør hvilket alternativ som er best for kunden.

#Definere variablene
fastpris1=750
fastpris2=300
fastpris3=150
kmPris1=2
kmPris2=4
antallKm=float(input('Hvor mange km har du kjørt?`'))

#Beregne priser
pris1=fastpris2+antallKm*kmPris1
pris2=fastpris3+antallKm*kmPris2

#Bestemme beste valget
if fastpris1<pris1 and fastpris1<pris2:
    print('fastpris er beste laternativet og vil koste',format(fastpris1,'.2f'))
else:
    if pris1<pris2 and pris1<fastpris1:
        print('Alternativ 2 er beste alternativet og vil koste',format(pris1,'.2f'))
    else:
        if pris2<pris1 and pris2<fastpris1:
            print('Alternativ 3 er beste alternativ og vil koste',format(pris2,'.2f'))
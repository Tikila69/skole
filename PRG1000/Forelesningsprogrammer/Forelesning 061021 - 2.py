#Program for å finne minste tall og tallnr. i en tallrekke på 5 tall
#Ønsker å plukke ut første gang tallet forekommer ved samme tall flere ganger

minstetall=1000
tallnr=0

for n in range (1,6,1):
    tall=int(input('Skriv inn ett tall: '))
    if tall<minstetall:
        minstetall=tall
        tallnr=n
    else:
        if tallnr==0:
            minstetall=tall
            tallnr=n
    print()

print('Minste tall er',minstetall,'og det er tallnr',tallnr,'i rekka')

#Om alle tallene er større enn dummy vil minstetall printes som dummy og tallnr vil være 0. Dårlig løsning
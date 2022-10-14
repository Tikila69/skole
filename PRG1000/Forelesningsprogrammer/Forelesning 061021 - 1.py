#Program for å finne minste tall og tallnr. i en tallrekke på 5 tall


#For å unngå å bruke dummy lar en første tallet man tar imot, også være laveste tallet til nå.
#Det gjør en i tilfellet utenfor FOR løkka

minstetall=int(input('Vennligst oppgi det første tallet i rekken: '))
tallnr=1
print()

for n in range (2,6,1):
    tall=int(input('Vennligst oppgi neste tallet i rekken: '))
    if tall<minstetall:
        minstetall=tall
        tallnr=n
    print()

print('Minste tall er',minstetall,'og det er tallnr',tallnr,'i rekka')

#Om alle tallene er større enn dummy vil minstetall printes som dummy og tallnr vil være 0. Dårlig løsning
#Oppgave 3
#Norsk matematikkråd har følgende retningslinjer for karaktersetting i kvantitative fag på Bachelornivå («poeng av 100»).

#Karakter	Poeng
#A	92
#B	77
#C	58
#D	46
#E	40
#Lag et program som på bakgrunn av poengsum som inndata viser kandidatens karakter i emnet.

#Definere variabler
poengsum=int(input('Hva er poengsummen til eleven? '))

#Bruk inndata for å bestemme karakter
if poengsum>=92:
    print('Elevens karakter er "A"')
else:
    if poengsum>=77:
        print('Elevens karakter er "B"')
    else:
        if poengsum>=58:
            print('Elevens karakter er "C"')
        else:
            if poengsum>=46:
                print('Elevens karakter er "D"')
            else:
                if poengsum>=40:
                    print('Elevens karakter er "E"')
                else:
                    print('Elevens karakter er "F"')
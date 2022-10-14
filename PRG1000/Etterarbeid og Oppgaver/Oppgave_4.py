#Lag et programm som tar imot 5 tall som inndata og som skriver ut verdien-
#og tallnummeret på det minste tallet

tall1=int(input('Skriv inn første tallet her: '))
tall2=int(input('Skriv inn andre tallet her: '))
tall3=int(input('Skriv inn tredje tallet her: '))
tall4=int(input('Skriv inn fjerde tallet her: '))
tall5=int(input('Skriv inn siste tallet her: '))

if tall1<=tall2:
    print(tall1)
else:
    if tall2<=tall3:
        print(tall2)
    else:
        if tall3<=tall4:
            print(tall3)
        else:
            if tall4<=tall5:
                print(tall4)
            else:
                if tall5<=tall1:
                    print(tall5)

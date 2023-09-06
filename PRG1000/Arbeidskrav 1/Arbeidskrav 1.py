#Starte løkken for at programmet skal kjøre inntil avsluttet.
fortsette="ja"

while fortsette=="ja":
    #Be om informasjon fra lånetaker om pris på bolig og inntekt
    pris=int(input('Hvor mye koster boligen? '))
    inntekt=int(input('Hva er din buttoinntekt? '))
    egenkapital=int(input('Hvor mye har du i egenkapital? '))
    print()
    
    #Gjør beregninger for hva som er nødvendig for lån
    lanesum=pris-egenkapital
    nodvendigEgenkapital=pris*0.15
    nodvendigInntekt=lanesum/5
    print('Det faktiske lånet vil komme på:',lanesum)
    print('Nødvendig Egenkapital for dette lånet er:',nodvendigEgenkapital)
    print('Nødvendig Inntekt for dette lånet er:',nodvendigInntekt)
    print()

    #kontrollere lånetakers informasjon opp imot kriterier
    if egenkapital<nodvendigEgenkapital:
        print('Lån ikke innvilget på bakgrunn av for lav egenkapital')
    else:
        if inntekt<nodvendigInntekt:
            print('Lån ikke innvilget på bakgrunn av for lav bruttoinntekt')
        else:
            if inntekt>=nodvendigInntekt and egenkapital>=nodvendigEgenkapital:
                print('Lånet er innvilget')
                print()

    #Spør om bruker ønsker å fortsette programmet
    fortsette=input('Ønsker du å fortsette programmet? ')
#Først trenger vi inndata fra brukeren
timelonn=float(input('Hva er din timelønn? '))
antallTimer=float(input('Hvor mange timer har du jobbe? '))

#Beregne bruttolønn
bruttolonn=timelonn*antallTimer

#Finne riktig skattesats
if bruttolonn<20000:
    skattesats=28
else:
    if bruttolonn<30000:
        skattesats=35
    else:
        skattesats=40

#Beregne skatt og nettolønn
skattIKroner=bruttolonn*skattesats/100
nettolonn=bruttolonn-skattIKroner

#skrive ut lønnsberegningen
print('Din bruttolønn er da:',format(bruttolonn,'.2f'))
print('Din skatteprosent er:',skattesats,'og skattetrekk i kr er:',format(skattIKroner,'.2f'))
print('Din nettolønn er:',format(nettolonn,'.2f'))


#En utleier av paintball (bane og utstyr) beregner sine priser på følgende måte:
#Leie av bane: 2.500 kr
#Tillegg pr deltaker: 420 kr
#Lag et program som beregner og skriver ut total pris basert på antall deltakere som inndata.

#Dersom det er 10 deltakere eller flere er tillegget pr deltaker 380 kr.
#Lag et program som beregner og skriver ut total pris basert på antall deltakere som inndata.

#Dersom det er 20 deltakere eller flere er tillegget pr deltaker 350 kr.
#Lag et program som beregner og skriver ut total pris basert på antall deltakere som inndata.

#Definer variabler
leie=2500
tillegg=420


#Få inndata fra bruker
deltakere=int(input('Hvor mange personer skal splle? '))

#Beregne pris.
if deltakere>=20:
    tillegg=350
else:
    if deltakere>=10:
        tillegg=380

pris=leie+tillegg*deltakere

#Print resultatet
print('Totalpris for leie inkl. tillegg:',format(pris,'.2f'))

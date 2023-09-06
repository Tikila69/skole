#En utleier av paintball (bane og utstyr) beregner sine priser på følgende måte:
#Leie av bane: 2.500 kr
#Tillegg pr deltaker: 420 kr
#Lag et program som beregner og skriver ut total pris basert på antall deltakere som inndata.


antall_deltakere = int(input("Hvor mange deltakere skal spille? "))

leie = 2500
tillegg = 420
svar = (antall_deltakere * tillegg) + leie

print("Totalpris for leie inkl. tillegg: ", svar, "kr")











#Definer variabler
leie=2500
tillegg=420

#Få inndata fra bruker
deltakere=int(input('Hvor mange personer skal splle? '))

#Beregne pris
pris=leie+tillegg*deltakere

#Print resultatet
print('Totalpris for leie inkl. tillegg:',format(pris,'.2f'))
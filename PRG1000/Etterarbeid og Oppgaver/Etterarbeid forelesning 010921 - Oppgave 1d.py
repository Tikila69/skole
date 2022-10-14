#En utleier av paintball (bane og utstyr) beregner sine priser på følgende måte:
#Leie av bane: 2.500 kr
#Tillegg pr deltaker: 420 kr
#Lag et program som beregner og skriver ut total pris basert på antall deltakere som inndata.

#Dersom det er 10 deltakere eller flere er tillegget pr deltaker 380 kr.
#Lag et program som beregner og skriver ut total pris basert på antall deltakere som inndata.

#Dersom det er 20 deltakere eller flere er tillegget pr deltaker 350 kr.
#Lag et program som beregner og skriver ut total pris basert på antall deltakere som inndata.

#Firmaet vurderer å gå over til en ny prisstrategi
#3.500 kr i baneleie og 350 kr pr deltaker for inntil 9 deltakere
#2.000 kr i baneleie og 400 kr pr deltaker fra 10 inntil 19 deltakere
#1.000 kr i baneleie og 450 kr pr deltaker fra 20 deltaker
#Maks kapasitet på en leieavtale er 30 deltakere.
#Lag et program som på bakgrunn av antall deltakere sammenligner og skriver ut pris etter
#gammel prisstrategi (a)-c)) og ny prisstrategi (d)) og skriver ut hvilken prisstrategi som
#er best for firmaet for det oppgitte deltakerantallet.


#Definer variabler
leieA=2500
tilleggA=420

leieB=3500
tilleggB=350


#Få inndata fra bruker
deltakere=int(input('Hvor mange personer skal splle? '))

#Prisberegning A
if deltakere>=20:
    tilleggA=350
else:
    if deltakere>=10:
        tillegg1=380

prisA=leieA+tilleggA*deltakere

#Prisberegning B
if deltakere>=20:
    leieB=1000
    tilleggB=450
else:
    if deltakere>=10:
        leieB=2000
        tilleggB=400

prisB=leieB+tilleggB*deltakere

#print resultatet

print('Totalpris format A er:',format(prisA,'.2f'))
print('Totalpris format B er:',format(prisB,'.2f'))

if prisA>prisB:
    print('Format A er det beste formatet for denne mengden deltakere')
else:
    print('Format B er det beste formatet for denne mengden deltakere')



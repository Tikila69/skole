#Beregning av antallet menn og kvinner i en gruppe i %

#Få antallet kvinner og menn fra brukeren
antallMenn=int(input('Hvor mange menn er det i gruppen? '))
antallKvinner=int(input('Hvor mange kvinner det i gruppen? '))

#Summer opp antall mennesker i gruppen
antallMennesker=antallMenn+antallKvinner

#Beregn prosentvis inndeling av menn og kvinner i gruppen
antallMennProsent=antallMenn/antallMennesker*100
antallKvinnerProsent=antallKvinner/antallMennesker*100

#Print resultatet av beregning
print('Menn: ',antallMennProsent)
print('Kvinner: ',antallKvinnerProsent)

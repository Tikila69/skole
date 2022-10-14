#Matematisk operatorer og operatorpresidense
#Vi bruker oppgavene i Checkpoint 2.19, s. 87

a=6+3*5
print('6+3*5=',a)

b=12/2-4
print('12/2-4=',b)

c=9+14*2-6
print('9+14*2-6=',c)

d=(6+2)*3
print('(6+2)*3=',d)

e=14/(11-4)
print('14/(11-4)=',e)

f=9+12*(8-3)
print('9+12*(8-3)=',f)

#formatering av desemialtall
prisPrKg=10.37
antallKg=9.6
totalpris=antallKg*prisPrKg
print('Totalpris=',totalpris)

#Utskrift av toitalpris avrunnet til 2 desimaler
print('Totalpris=',format(totalpris,'.2f'))

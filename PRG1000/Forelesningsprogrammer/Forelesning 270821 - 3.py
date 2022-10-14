#Alternativ fremgangsmåte for oppgave 2-17, s. 82, Alternativ fremgangsmåte 1
#Bruk av variable som holder orden på gjenværende sekunder etter en konvertering

#Gjøre om sekunder til timer, minutter og sekunder

#Be brukeren oppgi antall sekunder
sekunderInput=int(input('skriv in antall sekunder: '))

#Beregn antall timer
timer=sekunderInput//3600
restSekunder=sekunderInput-3600*timer

#Beregn antall gjenværende minutter og sekunder
minutter=restSekunder//60
sekunder=restSekunder-60*minutter

#Print resultatet
print(timer,'time(r),',minutter,'minutt(er),',sekunder,'sekund(er).')

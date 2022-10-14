#Alternativ fremgangsmåte for oppgave 2-17, s. 82, Alternativ fremgangsmåte 2
#Bruk av variable som holder orden på gjenværende sekunder etter en konvertering

#Gjøre om sekunder til timer, minutter og sekunder

#Be bruker oppgi antall sekunder
sekunderInput=int(input('Oppgi antall sekuinder som skal konverteres: '))

#Beregne antall timer
timer=sekunderInput//3600
restSekunder=sekunderInput%3600

#beregne antall minutter og sekunder
minutter=restSekunder//60
sekunder=restSekunder%60

#Print resultatet av konverteringen
print(timer,'time(r)',minutter,'minutt(er)',sekunder,'sekund(er)')

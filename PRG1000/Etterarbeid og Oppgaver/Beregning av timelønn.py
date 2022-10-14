#Beregning av bruttolønn

#Først trenger vi input/inndata fora brukeren

timelonn=int(float(input('Hva er din timelønn? ')))
antall_timer=int(float(input('Hvor mange timer har du arbeidet? ')))

#Beregne bruttolønn
bruttolonn=timelonn*antall_timer

#Skrive ut lønnsberegningen
print('Din bruttolønn er da',bruttolonn)

#Variabelnavn notasjon/konvensjon, enten antall_timer eller antallTimer ("lowercamelCase")
#Float kan brukes for å kunne inputte desimaler i tall

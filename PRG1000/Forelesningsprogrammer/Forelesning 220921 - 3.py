#Program som simulerer test av disjunksjonen/ELLER mellom 2 logiske utsagnt

print('Vi ønsker å vurdere A>3 ELLER B<6 for ulike verdier av A og B, jfr forelesning 4 onsdag 080921')

#I dette eksempelet bryter vi med at variabelnavn bør skrive med små bokstaver

#Verdien på A styres av en FOR-løkke fom. verdien 2 tom. verdien 5
for A in range (2,6,1):
    print()
    #Verdien på B styres av en FOR-løkke fom. verdien 5 tom. verdien 7
    for B in range (4,8,1):
        if A>3 or B<6:
            print('Disjunksjonene er sann')
        else:
            print('Disjunksjonen er usann')
print()
print('Programmet er ferdig')
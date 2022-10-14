import random

antKron=0
antMynt=0

antKast=int(input("Hvor mange kast? "))

for antallGanger in range (1,antKast+1):
    if random.randint(0,1)==0:
        sideOpp="krone"
        antKron+=1
    else:
        sideOpp="Mynt"
        antMynt+=1
    print("Resultatet av kast nr",antallGanger,"ble",sideOpp)
print("Resultater ble",antKron,"antall krone og",antMynt,"antall mynt")
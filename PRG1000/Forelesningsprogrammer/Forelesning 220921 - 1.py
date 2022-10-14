#To variable for å holde orden på misnte tall og tallnr. Begge settes lik 0
misnt=0
tallnr=0

#Fem vilkårlige tall som inndata
t1=int(input('Oppgi tall 1: '))
t2=int(input('Oppgi tall 2: '))
t3=int(input('Oppti tall 3: '))
t4=int(input('Oppgi tall 4: '))
t5=int(input('Oppgi tall 5: '))

#Så tester for å finne minste tall og tallnr.

if t1>t2:
    minst=t2
    tallnr=2
else:
    minst=t1
    tallnr=1
if t3<minst:
    minst=t3
    tallnr=3
if t4<minst:
    minst=t4
    tallnr=4
if t5<minst:
    minst=t5
    tallnr=5

#Så skriver vi ut resultatet, minste tall og tallnr.
print('Det minste tallet er',minst,'som har tallnr',tallnr)

#Tegn programkart
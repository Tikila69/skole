#Lag et program som tar imot 5 tall som inndata, og som skriver ut verdien og "tallnr" på det 
#minste tallet.

#Definere input

tall=0
minst=int(input('Skriv inn det første tallet: '))
minstN=1
print()
for n in range (1,5,1):
    tall=int(input('Skriv inn det neste tallet: '))
    if tall<minst:
        minst=tall
        minstN=n+1
    print()


print('Det minste tallet er:',minst,'og har posessjon:',minstN)
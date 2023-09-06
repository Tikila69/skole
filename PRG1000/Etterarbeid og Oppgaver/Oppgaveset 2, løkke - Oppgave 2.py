#Lag et program som tar imot 5 tall som inndata, og som skriver ut verdien og "tallnr" på det 
#minste tallet.

#Definere input

tall=int(input('Skriv inn det første tallet: '))


minst=tall
for n in range (1,5,1):
    tall=int(input('Skriv inn det neste tallet: '))
    if tall<minst:
        minst=tall


print('Det minste tallet er:',minst)




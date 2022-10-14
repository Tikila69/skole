#definere variabler
tall=int(input('Definer ett tall: '))

#definere tallene med IF statements
if tall>0:
    print('Tallet er positivt')
else:
    if tall<0:
        print('Tallet er negativt')
    else:
        print('Tallet er lik 0')

if tall%2==0:
    print('Tallet er ett heltall')
else:
    print('Tallet er ett oddetall')
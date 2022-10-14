#Be om massen til objektet
masse=float(input('Hva er massen til objektet? '))

#regne tom til newton
vekt=masse*9.8

#sette inn regler for vekt
if vekt>500:
    print('Error! Vekt overskrider 500 newton')
else:
    if vekt<100:
        print('Error! Vekt er under 100 newton')
    else:
        print('Vekten på objektet omgjort til newton:',vekt)
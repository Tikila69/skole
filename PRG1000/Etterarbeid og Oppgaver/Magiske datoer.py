# få inndata fra bruker
dag = int(input('Skriv inn en dag med 2 siffer: '))
maaned = int(input('Skriv inn en måned med 2 siffer: '))
aar = int(input('Skriv inn ett år med 2 siffer: '))

# beregn om året er magisk

if dag*maaned == aar:
    print('Datoen er magisk!')
else:
    print('Datoen er ikke magisk')

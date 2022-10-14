#Inndatatest i begynnelsen på programmet

#Variabel til bruk til inndatatest, bols variabel
nyttTall=True

#Løkke som sikrer oss gyldig verdi
while nyttTall:
    #Brukeren oppgir verdi på ruletten
    tall=int(input('Hva er tallet på ruletten? '))

    #tester om gyldig verdi
    if tall>=0 and tall<=36:
        print('Gyldig verdig')
        nyttTall=False
    else:
        print('Ugyldig verdig, vennligst oppgi et gyldig tall mellom 0 og 36.')

print('Beregner farge på tallet...')
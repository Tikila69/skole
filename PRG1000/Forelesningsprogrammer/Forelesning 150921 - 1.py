#Progra"m for å beregne farge på tall på ruletten

#Alternativ 3. tar utgangspunkt i hvilke farger gjelder for hvilke intervaller og "talltype"

#1 test på farge, dvs sann/usann på if-test nr. 3
#Kan da ikke si om tallet er partall eller oddetall eller hvilket intervall det tilhører. Kun farge

#Brukeren oppgir verdi på rulletten
tall=int(input('Hva er tallet på rullette? '))

#Er tallet et gyldig tall?
if tall>=0 and tall<=36:
    if tall==0:
        print('Tallet er markert grønn på ruletten')
    else:
        #Hele IF-setningen deles over flere linjer, må da stå i ekstra parantes
        if ((tall>=1 and tall<=10 and (tall%2)==0)
        or (tall>=11 and tall<=18 and (tall%2)!=0)
        or (tall>=19 and tall<=28 and (tall%2)==0)
        or (tall>=29 and tall<=36 and (tall%2)!=0)):
            print('Tallet er merket svart i ruletten')
        else:
            print('Tallet er merket rødt i rulletten')
else:
    print('Tallet er ikke et gyldig tall')
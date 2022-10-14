#Oppgave 4
#Lag et program som tar imot 5 tall som inndata, og som skriver ut verdien og "tallnr" på det minste tallet.

#Definere inndata
tall1=int(input('Definer tall nr. 1: '))
tall2=int(input('Definer tall nr. 2: '))
tall3=int(input('Definer tall nr. 3: '))
tall4=int(input('Definer tall nr. 4: '))
tall5=int(input('Definer tall nr. 5: '))

if tall1<tall2 and tall1<tall3 and tall1<tall4 and tall1<tall5:
    print('Tall 1 er det laveste tallet med verdi:',tall1)
else:
    if tall2<tall1 and tall2<tall3 and tall2<tall4 and tall2<tall5:
        print('Tall 2 er det laveste tallet med verdi:',tall2)
    else:
        if tall3<tall1 and tall3<tall2 and tall3<tall4 and tall3<tall5:
            print('Tall 3 er det laveste tallet med verdi:',tall3)
        else:
            if tall4<tall1 and tall4<tall2 and tall4<tall3 and tall4<tall5:
                print('Tall 4 er det laveste tallet med verdi',tall4)
            else:
                if tall5<tall1 and tall5<tall2 and tall5<tall3 and tall5<tall4:
                    print('Tall 5 er det laveste tallet med verid:',tall5)
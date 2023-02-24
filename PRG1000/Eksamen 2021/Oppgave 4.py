def regusterer_ny_kunde():
    #Løkke for registrering av kunder
    registrering='j'
    while registrering=='j':

        #Løkke for duplikatkontroll
        kontroll='j'
        while kontroll=='j':
            #Åpne fil
            kunde=open('kunde.txt','r')
            
            #Be om input fra bruker 
            mobilnr=input('Oppgi mobilnummer: ')
            
            #Definere bolsk variabel for å håndtere duplikatkontroll
            duplikatkontroll=True

            #Les filen og let etter duplikat
            kundesok=kunde.readline()

            while kundesok!='':

                if mobilnr==kundesok.rstrip('\n'):
                    print('Kunde allerede registert på dette telefonnummeret')
                    duplikatkontroll=False
                kundesok=kunde.readline()

            #Om duplikat finnes, spør om nytt søk skal gjennomføres
            if duplikatkontroll==False:
                kontroll=input('Ønsker du å prøve et annet telefonnummer? (j/n): ')
                if kontroll!='j':
                    registrering='n'

            #Dersom ingen duplikat er funnet, spør om det skal registeres dekk på kunde.
            if duplikatkontroll==True:
                kontroll='n'
                kunde.close()
                registereDekk=input('Ønsker du å registere dekk på kunde? (j/n): ')


                #Dersom dekk skal registeres, be om resterende informasjon for registering fra bruker.
                if registereDekk=='j':
                    kunde=open('kunde.txt','a')
                    oppbevaring=open('oppbevaring.txt','a')
                    dekksett=open('dekksett.txt','a')
                    fornavn=input('Oppgi fornavn: ')
                    etternavn=input('Oppgi etternavn: ')
                    epost=input('Oppgi epost: ')
                    regnr=input('Oppgi registeringsnummer: ')
                    dato=input('Oppgi dato for innlevering: ')
                    hylle=input('Oppgi hylle: ')
                    pris=input('Oppgi pris: ')

                    #Skriv oppgitt informasjon til sine respekte filer
                    kunde.write(mobilnr+'\n'+fornavn+'\n'+etternavn+'\n'+epost+'\n')
                    oppbevaring.write(mobilnr+'\n'+regnr+'\n'+dato+'\n'+'X'+'\n'+pris+'\n')
                    dekksett.write(mobilnr+'\n'+regnr+'\n')
                    kunde.close()
                    oppbevaring.close()
                    dekksett.close()

                    #Tilbakemelding til bruker samt spørsmål om ny registereing skal finne sted.
                    print()
                    print('Registereing fullført')
                    registrering=input('Ønsker du å registere en ny kunde? (j/n): ')

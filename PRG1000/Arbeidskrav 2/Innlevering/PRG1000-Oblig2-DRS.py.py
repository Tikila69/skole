#Underprogram nr. 1: Studentregistrering
def studentregistrering():
    #Løkke for å la programmet kjøre så lenge bruker ønsker.
    reglokke='j'
    while reglokke=='j':

        #Løkke for å kontrollere at studentnummer ikke allereder i bruk.
        idKontroll='j'
        while idKontroll=='j':

            #Åpne filen og be om studentnummer fra bruker
            student=open('student.txt','r')
            studentnummer=input('Skriv inn gyldig studentnummer: ')
            print()

            #Be programmet lese første linjen i filen.
            studnrKontroll=student.readline()

            #Definere en bolk variabel for å kontrollere om studentnummer lagt inn allereder i bruk.
            studentnrUbrukt=True

            #Løkke for å lese gjennom hele filen i søk etter studentnummer.
            while studnrKontroll!='':
                if studentnummer==studnrKontroll.rstrip('\n'):
                    print('Studentnummeret er i bruk')
                    idKontroll=input('Ønsker du å prøve et annet nummer? (j/n)? ')
                    if idKontroll=='n':
                        reglokke='n'
                    studentnrUbrukt=False
                studnrKontroll=student.readline()

            #Dersom studentnummeret er ubrukt, be om resten av informasjonen fra bruker, stenge filen og åpne den i "a" for å kunne legge til ny student.
            if studentnrUbrukt==True:
                idKontroll='n'
                student.close()
                student=open('student.txt','a')
                fornavn=input('Oppgi fornavn: ')
                etternavn=input('Oppgi etternavn: ')
                studium=input('Oppgi studium: ')
                
                #Skrive inn studentinformasjonen i filen og gi tilbakemelding til bruker når utført
                student.write(studentnummer+'\n'+fornavn+'\n'+etternavn+'\n'+studium)
                student.close()
                print()
                print('Registrering fullført')

                #Spørre om bruker ønsker å fortsette programmet.
                reglokke=input('Ønsker du å legge inn en ny student? (j/n): ')


#Definere delprogram 2: Studentsøk
def studentsok():

    #Løkke for å la programmet kløre så lenge bruker ønsker.
    nyttSok='j'
    while nyttSok=='j':

        #Løkke for å kontrollere at oppgitt studentnummer er et gyldig studentnummer.
        studnrGyldig='j'
        while studnrGyldig=='j':

            #Be bruker oppgi studentnummer for søket.
            studentnummer=input('Oppgi studentnummer til studenten: ')
            print()
            
            #Åpne  nødvendige filer for søket
            studenter=open('student.txt','r')
            emner=open('emne.txt','r')
            resultater=open('eksamensresultater.txt','r')

            #Definere en bolsk variabel for å vite om søket har gitt resultater eller ikke.
            funnet=False
            
            #Be programmet lese første linjen i student.txt filen.
            student=studenter.readline()

            #Løkke for p lese hele filen og definere de forskjellige linjene i filen med hva som står i dem.
            while student!='':
                fornavn=studenter.readline()
                etternavn=studenter.readline()
                studium=studenter.readline()

                #Dersom søk gir resulateter, print nødvendig informasjon og definer bolsk variabel =True
                if student.rstrip('\n')==studentnummer:
                    funnet=True
                    print('Navn:',fornavn.rstrip('\n'),etternavn.rstrip('\n'))
                    print('Studentnummer:',student.rstrip('\n'))
                    print('Studium:',studium.rstrip('\n'))
                    studium=studenter.readline()
                    studnrGyldig='n'
                student=studenter.readline()

            #Dersom søk ikke gir resultater informer bruker og spør om de ønsker å foreta et nytt søk.
            if funnet==False:
                print('Ingen studenter med dette studentnummeret er funnet i systemet.')
                print('Ønsker du å foreta et nytt søk?')
                studnrGyldig=input('j/n: ')
                if studnrGyldig=='n':
                    nyttSok='n'
            
            #Dersom søk gir resultater, begyn å lese fil "eksamensresultater.txt" ved hjelp av studentnummer for å finne karakterer og emnekoder.
            else:
                emnekodeEksamen=resultater.readline()
                resultaterFunnet=False

                #Løkke for å lese filen frem til E.O.L. merket og definere hver linjes innhold.
                while emnekodeEksamen!='':
                    studentnr=resultater.readline()
                    karakter=resultater.readline()

                    #Dersom studentnummer i filen er likt studentnummer søkt på tidligere i programmet, print ut emnekode og karakterer for bruker.
                    if studentnr.rstrip('\n')==studentnummer:
                        resultaterFunnet=True
                        print('Resultater: Emnekode;',emnekodeEksamen.rstrip('\n'),'karakter;',karakter.rstrip('\n'))
                        
                        #Om karakterer er funnet, begynn lesing av "emne.txt" filen for å finne emmnenavnet ved help av emnekode fra "eksamensresulater.txt" filen.
                        emne=emner.readline()

                        #Løkke for å lese hele filen til E.O.L merket og definere innholdet i hver linje lest.
                        while emne!='':
                            emnenavn=emner.readline()
                            
                            #Dersom emnekode fra "eksamensresultater.txt" tilsvarer emnekode fra "emne.txt", print ut emnekode og emnenavn.
                            if emne.rstrip==emnekodeEksamen.rstrip('\n'):
                                print(emnekodeEksamen,'-',emnenavn)
                                emne=emner.readline()
                            emne=emner.readline()
                    
                    #først når "emne.txt" fil er lest og korrekt emnenavn er printet, kan man lese neste linje i "eksamensresultater.txt" filen for å finne
                    #flere resultater på studenten.
                    emnekodeEksamen=resultater.readline()
                
                #Dersom søket ikke gir resulater, informer bruker og spør om bruker ønsker å foreta et nytt søk.
                if resultaterFunnet==False:
                    print('Ingen eksamensresultater funnet på denne studenten')
                
                #Steng filene etter lesing for å resette lesermerke.
                studenter.close()
                emner.close()
                resultater.close()
                nyttSok=input('Ønsker du å foreta et nytt søk? j/n: ')


#Definere delprogram 3: Studentsletting.
def studentsletting():

    nyttSok='j'

    #Løkke for å la programmet kjøre så lenge bruker ønsker.
    while nyttSok=='j':

        #Be om studentnummer fra bruker.
        studentnr=input('Skriv inn studentnummeret på studenten du ønsker å slette: ')
        print()

        #Definere en bolks variabel for å se om bruker har registrerte eksamensresultater.
        funnet=False

        #Åpne "eksamensresulater.txt" for å finne ut om bruker har registrerte eksamensresulater.
        studentSletting=open('eksamensresultater.txt','r')
        kontroll=studentSletting.readline()

        #Løkke for å la programmet lese hele filen til E.O.L. merket.
        while kontroll!='':

            #Dersom programmet finner brukeren i filen, definer bolsk variabel=True
            if kontroll.rstrip('\n')==studentnr:
                funnet=True
            kontroll=studentSletting.readline()

        #Dersom studentnummeret ikke er funnet i filen, informer bruker om at studenten ikke har eksamensresultater registrert på seg og kan derfor slettes.
        if funnet==False:
            print('Studenten har ingen eksamensresultater registrert')
            print()
            
            #Spør om bruker ønsker å slette studenten.
            print('Ønsker du å slette studenten?')
            slette=input('j/n: ')

            #Dersom bruker svarer "ja", steng "eksamensresultater.txt" og åpne "student.txt" samt en temp fil "temp.txt"
            if slette=='j':
                studentSletting.close()
                studentSletting=open('student.txt','r')
                tempfil=open('temp.txt','w')
                funnet=False

                #importere os for å la programmet endre navn på og slette filer.
                import os
                studentnummer=studentSletting.readline()

                #Løkke for å la programmet lese "student.txt" filen frem til E.O.L. merket, samt definere hva hver linje i filen inneholder.
                while studentnummer!='':
                    fornavn=studentSletting.readline()
                    etternavn=studentSletting.readline()
                    studium=studentSletting.readline()

                    #Dersom studentnummeret fra søket tidligere i programmet ikke samsvarer med ett studentnummer i filen, skriv informasjonen til studenten
                    #over til "temp.txt" filen.
                    if studentnummer.rstrip('\n')!=studentnr:
                        tempfil.write(studentnummer+fornavn+etternavn+studium)
                    studentnummer=studentSletting.readline()

                #Steng "temp.txt" filen for å lagre skrivingen til filen.
                tempfil.close()

                #Steng "student.txt" filen.
                studentSletting.close()

                #La programmet slette "student.txt" filen
                os.remove('student.txt')

                #La programmet endre navnet fra "temp.txt" til "student.txt"
                os.rename('temp.txt','student.txt')

                #Gi bruker beskjed om at sletting er gjennomført
                print('Student slettet.')
                print()

                #Spør om bruker ønsker på slette en ny student.
                print('Ønsker du å slette en annen student?')
                nyttSok=input('j/n: ')

        #Dersom bruker har eksamensresulateter registrert, informer bruker om an studenten ikke kan slettes.            
        else:
            print('Studenten har eksamenskarakterer registrert og kan derfor ikke slettes')
            print()

            #Spør om bruker ønsker å gjennomføre et nytt søk.
            print('Ønsker du å søke opp en annen student?')
            studentSletting.close()
            nyttSok=input('j/n: ')


#Bolks variable for å tillate løkke og la programmet kjøre så lenge bruker ønsker.
fortsette=True

print('Hei! Velkommen til denne studentdatabasen')
print()
print('Under ser du 4 valg. Skriv inn korresponderende tall for å fortsette')
print()

#Løkke som tillater programmet å kjøre så lenge bruker ønsker det.
while fortsette==True:

    #Informer bruker om hvilke programmer bruker har tilgang til.
    print('...................................................................................................')
    print('Studentregistrering: 1')
    print()
    print('Studentsøk: 2')
    print()
    print('Studentslett: 3')
    print()
    print('Exit: 9')
    print('...................................................................................................')

    #Be bruker fylle inn nummmer som tilsvarer hvilket program de ønsker å kjøre.
    valg=int(input('Fyll inn tall her: '))
    if valg==1:
        print('Du har valgt "Studentregistrering"')
        print()
        studentregistrering()
    if valg==2:
        print('Du har valgt "Studentsøk"')
        print()
        studentsok()
    if valg==3:
        print('Du har valg "Studentsletting"')
        print()
        studentsletting()

    #Dersom bruker velger 9, definer fortsette=False for å la stenge løkke.
    if valg==9:
        fortsette=False

    #Dersom bruker skriver inn et nummer som ikke tilsvarer et program, informer bruker og tillat bruker å prøve et nytt valg.
    if valg!=1 or 2 or 3 or 9:
        print('Vennligst oppgi et gyldig nummer for å fortsette')
        print()
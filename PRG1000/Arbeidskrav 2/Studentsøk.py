nyttSok='j'
while nyttSok=='j':

    studnrGyldig='j'
    while studnrGyldig=='j':

        studentnummer=input('Oppgi studentnummer til studenten: ')
        print()
        studenter=open('student.txt','r')
        emner=open('emne.txt','r')
        resultater=open('eksamensresultater.txt','r')
        funnet=False
        student=studenter.readline()
        while student!='':
            fornavn=studenter.readline()
            etternavn=studenter.readline()
            studium=studenter.readline()
            if student.rstrip('\n')==studentnummer:
                funnet=True
                print('Navn:',fornavn.rstrip('\n'),etternavn.rstrip('\n'))
                print('Studentnummer:',student.rstrip('\n'))
                print('Studium:',studium.rstrip('\n'))
                studium=studenter.readline()
                studnrGyldig='n'
            student=studenter.readline()
        if funnet==False:
            print('Ingen studenter med dette nummer er funnet i systemet.')
            print('Ønsker du å foreta et nytt søk?')
            studnrGyldig=input('j/n: ')
        else:
            emnekodeEksamen=resultater.readline()
            resultaterFunnet=False
            while emnekodeEksamen!='':
                studentnr=resultater.readline()
                karakter=resultater.readline()
                if studentnr.rstrip('\n')==studentnummer:
                    resultaterFunnet=True
                    print('Resultater: Emnekode;',emnekodeEksamen.rstrip('\n'),'karakter;',karakter.rstrip('\n'))
                    emne=emner.readline()
                    while emne!='':
                        emnenavn=emner.readline()
                        if emne.rstrip==emnekodeEksamen.rstrip('\n'):
                            print(emnekodeEksamen,'-',emnenavn)
                            emne=emner.readline()
                        emne=emner.readline()
                emnekodeEksamen=resultater.readline()
            if resultaterFunnet==False:
                print('Ingen eksamensresultater funnet på denne studenten')
            
            studenter.close()
            emner.close()
            resultater.close()
        nyttSok=input('Ønsker du å foreta et nytt søk? j/n: ')
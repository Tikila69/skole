#Program for sletting av studenter uten registrerte eksamensresultater
nyttSok='j'
while nyttSok=='j':
    studentnr=input('Skriv inn studentnummeret på studenten du ønsker å slette: ')
    funnet=False
    studentSletting=open('eksamensresultater.txt','r')
    kontroll=studentSletting.readline()
    while kontroll!='':
        if kontroll.rstrip('\n')==studentnr:
            funnet=True
        kontroll=studentSletting.readline()
    if funnet==False:
        print('Studenten har ingen eksamensresultater registrert')
        print('Ønsker du å slette studenten?')
        slette=input('j/n: ')
        if slette=='j':
            studentSletting.close()
            studentSletting=open('student.txt','r')
            tempfil=open('temp.txt','w')
            funn=False
            import os
            studentnummer=studentSletting.readline()
            while studentnummer!='':
                fornavn=studentSletting.readline()
                etternavn=studentSletting.readline()
                studium=studentSletting.readline()
                if studentnummer.rstrip('\n')!=studentnr:
                    tempfil.write(studentnummer+fornavn+etternavn+studium)
                studentnummer=studentSletting.readline()
            tempfil.close()
            studentSletting.close()
            os.remove('student.txt')
            os.rename('temp.txt','student.txt')
            print('Student slettet.')
            print()
            print('Ønsker du å slette en annen student?')
            nyttSok=input('j/n: ')
                    
    else:
        print('Studenten har eksamenskarakterer registrert og kan derfor ikke slettes')
        print()
        print('Ønsker du å søke opp en annen student?')
        studentSletting.close()
        nyttSok=input('j/n: ')
        

    
        
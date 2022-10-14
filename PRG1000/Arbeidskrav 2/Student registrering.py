reglokke='j'
while reglokke=='j':
    idKontroll='j'
    while idKontroll=='j':
        
        student=open('student.txt','r')
        studentnummer=input('Skriv inn gyldig studentnummer: ')
        studnrKontroll=student.readline()
        studentnrUbrukt=True
        while studnrKontroll!='':
            if studentnummer==studnrKontroll.rstrip('\n'):
                print('Studentnummeret er i bruk')
                idKontroll=input('Ønsker du å prøve et annet nummer? (j/n)? ')
                studentnrUbrukt=False
            studnrKontroll=student.readline()
        if studentnrUbrukt==True:
            idKontroll='n'
            student.close()
            student=open('student.txt','a')
            fornavn=input('Oppgi fornavn: ')
            etternavn=input('Oppgi etternavn: ')
            studium=input('Oppgi studium: ')
            student.write(studentnummer+'\n'+fornavn+'\n'+etternavn+'\n'+studium)
            student.close()
            print()
            print('Registrering fullført')
            reglokke=input('Ønsker du å legge inn en ny student? (j/n): ')
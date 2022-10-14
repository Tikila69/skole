def skrivKarakterliste(skriv_karakterliteStudentnr):

        studenter=open('student.txt','r')
        emner=open('emne.txt','r')
        resultater=open('eksamensresultater.txt','r')

        resultaterFunnet=False

        student=studenter.readline()
        while student!='':
            fornavn=studenter.readline()
            etternavn=studenter.readline()
            studium=studenter.readline()
            if student.rstrip('\n')==skriv_karakterliteStudentnr:
                print('Navn:',fornavn.rstrip('\n'),etternavn.rstrip('\n'))
                print('studentnr:',student.rstrip('\n'))
                print('Studium:',studium.rstrip('\n'))
                studium=studenter.readline()
            student=studenter.readline()
        else:
            emnekodeEksamen=resultater.readline()
            while emnekodeEksamen!='':
                studentnr=resultater.readline()
                karakter=resultater.readline()
                if studentnr.rstrip('\n')==skriv_karakterliteStudentnr:
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

def main():
    fortsette=True
    while fortsette==True:
        funnet=False
        student=open("student.txt","r")
        studentnr=input("Oppgi studentnr på student du ønsker å printe karakterliste på: ")
        studentnummer=student.readline()
        while studentnummer!="":
            fornavn=student.readline()
            etternavn=student.readline()
            studium=student.readline()
            if studentnummer.rstrip("\n")==studentnr:
                funnet=True
            studentnummer=student.readline()
        if funnet==True:
            student.close()
            skrivKarakterliste(studentnr)
            print("Ønsker du å søke opp et annet studentnr?")
            valg=input("j/n: ")
        if funnet==False:
            student.close()
            print('Ugyldig studentnummer')
            print()
            print("Ønsker du å søke opp et annet studentnr?")
            valg=input("j/n: ")
        if valg=="n":
            fortsette=False

main()
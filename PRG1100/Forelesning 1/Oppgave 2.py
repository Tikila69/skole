def skrivKarakterliste(studentnr):

        studenter=open('student.txt','r')
        emner=open('emne.txt','r')
        resultater=open('eksamensresultater.txt','r')

        resultaterFunnet=False

        student=studenter.readline()
        while student!='':
            fornavn=studenter.readline()
            etternavn=studenter.readline()
            studium=studenter.readline()
            if student.rstrip('\n')==studentnr:
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
                if studentnr.rstrip('\n')==studentnr:
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

def sjekkStudent(studentnr):
    funnet=False
    student=open("student.txt","r")

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
        return funnet

    if funnet==False:
        student.close()
        return funnet

def main():
    fortsette=True
    while fortsette==True:
        studentnr=input("Oppgi studentnr på student du ønsker å printe karakterliste på: ")
        sjekkStudent(studentnr)

        Status=sjekkStudent(studentnr)

        if Status==True:
            print("Studentnummer Status")
            skrivKarakterliste(studentnr)

        if Status==False:
            print('Ugyldig studentnummer')
            print()
            print("Ønsker du å søke opp et annet studentnr?")
            valg=input("j/n: ")
            if valg=="n":
                fortsette=False

main()
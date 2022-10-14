def skrivEksamensresultater(skriv_eksamensresultaterStudentnr):
     
            studenter=open('student.txt','r')
            emner=open('emne.txt','r')
            resultater=open('eksamensresultater.txt','r')
            
            student=studenter.readline()
            while student!='':
                fornavn=studenter.readline()
                etternavn=studenter.readline()
                studium=studenter.readline()

                if student.rstrip('\n')==skriv_eksamensresultaterStudentnr:
                    print('Navn:',fornavn.rstrip('\n'),etternavn.rstrip('\n'))
                    print('Studentnummer:',student.rstrip('\n'))
                    print('Studium:',studium.rstrip('\n'))
                    studium=studenter.readline()

                    emnekodeEksamen=resultater.readline()
                    resultaterFunnet=False
                    while emnekodeEksamen!='':
                        studentnr=resultater.readline()
                        karakter=resultater.readline()
                        if studentnr.rstrip('\n')==skriv_eksamensresultaterStudentnr:
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
                student=studenter.readline()

def sjekkStudent():
    funnet=False
    studnr=input("Oppgi studentnummer: ")

    student=open("student.txt","r")

    studenten=student.readline()
    while studenten!="":
        if studenten.rstrip("\n")==studnr:
            funnet=True
        studenten=student.readline()
    return funnet,studnr

def main():

    fortsette=True
    while fortsette==True:
        status,studentnr=sjekkStudent()
        print("Resultat etter sjekkStudent():",status,studentnr)

        if status==True:
            skrivEksamensresultater(studentnr)
        else:
            print("Studenten finnes ikke")
        print("----------------------------------------------------------")
        print("Ønsker du å søke opp en ny student?")
        nyttSok=input("(j/n): ")
        if nyttSok=="n":
            fortsette=False

main()
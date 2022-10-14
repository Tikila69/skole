class Student:
    def __init__(self,studentnr,fornavn,etternavn,epost,studium):
        self.__studentnr=studentnr
        self.__fornavn=fornavn
        self.__etternavn=etternavn
        self.__epost=epost
        self.__studium=studium

    def __str__(self):
        return "Objektets atributter er: "+self.__studentnr+"\n"+self.__fornavn+"\n"+self.__etternavn+"\n"+self.__epost+"\n"+self.__studium

studentnr=input("Oppgi studentnr: ")
fornavn=input("Oppgi fornavn: ")
etternavn=input("Oppgi etternavn: ")
epost=input("Oppgi epost: ")
studium=input("Oppgi studium: ")

nyStudent=Student(studentnr,fornavn,etternavn,epost,studium)

print(nyStudent)

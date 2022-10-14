class Student:
    def __init__(self,studentnr,fornavn,etternavn,epost,studium):
        self.__studentnr=studentnr
        self.__fornavn=fornavn
        self.__etternavn=etternavn
        self.__epost=epost
        self.__studium=studium

    def __str__(self):
        return "Objektets atributter er: "+self.__studentnr+"\n"+self.__fornavn+"\n"+self.__etternavn+"\n"+self.__epost+"\n"+self.__studium

    def setStudentnr(self,studentnr):
        self.__studentnr=studentnr
    def getStudentnr(self):
        return self.__studentnr

    def setFornavn(self,fornavn):
        self.__fornavn=fornavn
    def getFornavn(self):
        return self.__fornavn

    def setEtternavn(self,etternavn):
        self.__etternavn=etternavn
    def getEtternavn(self):
        return self.__etternavn

    def setEpost(self,epost):
        self.__epost=epost
    def getEpost(self):
        return self.__epost

    def setStudium(self,studium):
        self.__studium=studium
    def getStudium(self):
        return self.__studium


studentnr=input("Oppgi studentnr: ")
fornavn=input("Oppgi fornavn: ")
etternavn=input("Oppgi etternavn: ")
epost=input("Oppgi epost: ")
studium=input("Oppgi studium: ")

nyStudent=Student(studentnr,fornavn,etternavn,epost,studium)

print(nyStudent)


print(nyStudent.getEpost())
print(nyStudent.getStudium())

epost=input("Oppgi ny epost: ")
nyStudent.setEpost(epost)

studium=input("Oppgi nytt studium: ")
nyStudent.setStudium(studium)

print(nyStudent)
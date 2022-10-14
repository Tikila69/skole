class Ansatt:
    def __init__(self,fornavn,etternavn,epost):
        self.__fornavn=fornavn
        self.__etternavn=etternavn
        self.__epost=epost
    
    def __str__(self):
        return "Objektets attributter er: "+self.__fornavn+"\n"+self.__etternavn+"\n"+self.__epost


ansattTextFil=open("ansattTextxFil.txt","r")
nyAnsattfil=open("nyansatte.dat","wb")
import random

class Mynt:
    def __init__(self):
        self.__sideopp=input("Hvilken side ligger opp? ")
    
    def kast(self):
        if random.randint(0,1)==0:
            self.__sideopp="Krone"
        else:
            self.__sideopp="Mynt"
    
    def hentSideopp(self):
        return(self.__sideopp)


def main():

    antKron=0
    antMynt=0
    
    minMynt=Mynt()

    print("Før første kast er denne siden opp:",minMynt.hentSideopp())

    antallkast=int(input("Hvor mange kast? "))

    for antallGanger in range (1,antallkast+1):
        minMynt.kast()

        print("Resultatet på kast nr:",antallGanger,"ble",minMynt.hentSideopp())

        if minMynt.hentSideopp()=="Krone":
            antKron+=1
        else:
            antMynt+=1
        
    print("Resultat:",antKron,"antall krone og",antMynt,"antall mynt")

main()
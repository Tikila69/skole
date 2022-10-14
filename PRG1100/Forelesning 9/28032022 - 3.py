import random

class Mynt:
    def __init__(self,sideopp):
        self.sideopp=sideopp
    
    def kast(self):
        if random.randint(0,1)==0:
            self.sideopp="Krone"
        else:
            self.sideopp="Mynt"
    
    def hentSideopp(self):
        return(self.sideopp)


def main():

    antKron=0
    antMynt=0

    sideopp=input("Hvilken side på mynten er opp? ")
    
    minMynt=Mynt(sideopp)

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
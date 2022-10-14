import pickle
class Bil:
    def __init__(self,regnr,merke,modell,startdato,posisjon):
        self.__regnr=regnr
        self.__merke=merke
        self.__modell=modell
        self.__startdato=startdato
        self.__posisjon=posisjon
    def getRegnr(self):
        return self.__regnr

bilfil=open("Bil.txt","r")
binærfil=open("bil.dat","wb")

regnr=bilfil.readline()

while regnr!="":
    regnr.rstrip("\n")
    merke=bilfil.readline().rstrip("\n")
    modell=bilfil.readline().rstrip("\n")
    startdato=bilfil.readline().rstrip("\n")
    posisjon=bilfil.readline().rstrip("\n")
    nybil=Bil(regnr,merke,modell,startdato,posisjon)
    pickle.dump(nybil,binærfil)
    regnr=bilfil.readline()

binærfil.close()
bilfil.close()


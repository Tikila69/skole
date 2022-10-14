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

datfila=open("bil.dat","rb")

fortsette=True
while fortsette==True:
    try:
        variabel=pickle.load(datfila)
        print(variabel.getRegnr())
    except EOFError:
        fortsette=False
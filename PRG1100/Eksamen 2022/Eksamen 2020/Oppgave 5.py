class Bil:
    def __init__(self,regnr,merke,modell,startdato,posisjon):
        self.__regnr=regnr
        self.__merke=merke
        self.__modell=modell
        self.__startdato=startdato
        self.__posisjon=posisjon
    def set_posisjon(self,posisjon):
        self.__posisjon=posisjon
    def get_posisjon(self):
        return self.__posisjon

nybil=Bil('SV123456','Opel','Astra','20210401','South Harley')
inndata=input('Skriv inn posisjon på bil: ')
nybil.set_posisjon(inndata)
print()
print(nybil.get_posisjon())
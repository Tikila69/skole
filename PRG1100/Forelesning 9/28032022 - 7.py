class BankKonto:
    def __init__(self,saldo) -> None:
        self.__saldo=saldo
    
    def innskudd(self,belop):
        self.__saldo=self.__saldo+belop

    def uttak(self,belop):
        if self.__saldo>=belop:
            self.__saldo=self.__saldo-belop
        else:
            print("Feil: You broke ass bitch")
    
    def hentSaldo(self):
        return(self.__saldo)
    

def main():

    saldo=float(input("Hva er saldoen på konto til kari? "))
    karisKonto=BankKonto(saldo)

    saldo=float(input("Hva er saldoen på konto til knut? "))
    knutsKonto=BankKonto(saldo)

    print("Kari har",karisKonto.hentSaldo(),"på konto")
    print("Knut har",knutsKonto.hentSaldo(),"på konto")

    belop=float(input("Hvor mye vil du legge inn på konto til Kari? "))
    karisKonto.innskudd(belop)
    print("Saldo på kontoen til Kari er:",karisKonto.hentSaldo())

    belop=(float(input("Hvor mye vil legge inn på konto til Knut? ")))
    knutsKonto.innskudd(belop)
    print("Saldo på konto til Knut er:",knutsKonto
    .hentSaldo())

    belop=float(input("Hvor mye skal Kari ta ut? "))
    karisKonto.uttak(belop)
    print("Saldoen på kontoen til kari er:",karisKonto.hentSaldo())

    belop=float(input("Hvor mye skal Knut ta ut? "))
    knutsKonto.uttak(belop)
    print("Saldoen på kontoen til Knut er:",knutsKonto.hentSaldo())

main()

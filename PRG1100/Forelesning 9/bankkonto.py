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
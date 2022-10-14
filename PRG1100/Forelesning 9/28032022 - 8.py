import bankkonto

def main():

    saldo=float(input("Hva er saldoen på konto til kari? "))
    karisKonto=bankkonto.BankKonto(saldo)

    saldo=float(input("Hva er saldoen på konto til knut? "))
    knutsKonto=bankkonto.BankKonto(saldo)

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
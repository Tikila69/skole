#Program for innføring i delprogrammer/funksjoner/prodedyrer

def drommebolig():
    #Her kommer kode for kalkulator 1
    print('Du har valgt kalkulator 1, Drømmebolig')
    print()

def lanebevis():
    #Her kommer kode for kalkulaltor 2
    print('Du har valgt kalkulator 2, Lånebevis')
    print()

def main():
    fortsette=True
    while fortsette==True:
        valgtKalkulator=int(input('Hvilken kalkulator ønsker du å bruke? '))
        if valgtKalkulator==1:
            drommebolig()
        else:
            lanebevis()

        svar=input('Ønsker du å bruke en av kalkulatorene på nytt? ')
        if svar=='nei':
            fortsette=False

#Her kalles hovedprogrammet main()
main()

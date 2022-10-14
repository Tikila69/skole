#program for å summere tall
antallTall=int(input('Hvor mange tall skal summeres? '))

summenEr=0

for n in range(1,antallTall+1,1):
    print('Tall nr:',n)
    tall=int(input('Oppgi tall: '))
    summenEr=summenEr+tall
    print()
print('summen av de',antallTall,'tallene er:',summenEr)
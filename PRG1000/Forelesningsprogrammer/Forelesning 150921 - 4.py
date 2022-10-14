#Program for å summere 5 tall

summenEr=0

for n in range(1,6,1):
    tall=int(input('Oppgi tall: '))
    summenEr=summenEr+tall
print('Summen av de 5 tallenen er:', summenEr)
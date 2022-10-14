#kode for oppgaveset 3 oppgave 2

student=[]
print('Studenter til nå:',student)
print()

nyStudent=True

while nyStudent==True:
    studnr=int(input('Oppgi student nummer: '))
    student+=[studnr]
    fnavn=input('Oppgi fornavn: ')
    student+=[fnavn]
    studiet=input('Oppgi studium: ')
    student+=[studiet]
    print('Studenter til nå:',student)
    print()

    svar=input('Skal det leses inn flere studenter? ')
    if svar=='nei':
        nyStudent=False

listelengdeStudent=len(student)
print()
print('Lista med studenter er',student,'og består av',int(listelengdeStudent/3),'registrete studenter')
print()

#Søke etter student på studentnummer
studnr=int(input('Oppgi studentnummer på student det skal søkes på: '))
funnet=False

for index in range (0,listelengdeStudent,3):
    if studnr==student[index]:
        funnet=True
        studenten=index
if funnet==True:
    print('Fullstendig informasjon om studenten er:')
    print('Studetnummer:',student[studenten])
    print('Fornavn:',student[studenten+1])
    print('Studium:',student[studenten+2])
else:
    print('Ingen studenter med oppgitt studentnummer er registrert')

#Prøv selv:
#1) Flytte print inn i FOR løkka
#2) Løse med While
#3) Søke etter studenter på studieprogram
import sys

liste=[]

try:
    studenter=open("studenter.txt","r",encoding=("utf-8"))
except IOError:
    print("Filen finnes ikke i målet")
else:

    studentnr=studenter.readline()

    while studentnr!="":
        studentnr=studentnr.rstrip("\n")
        fornavn=studenter.readline().rstrip("\n")
        etternavn=studenter.readline().rstrip("\n")
        epost=studenter.readline().rstrip("\n")
        fødselsdato=studenter.readline().rstrip("\n")
        kjønn=studenter.readline().rstrip("\n")
        studium=studenter.readline().rstrip("\n")

        liste+=[[studentnr,fornavn,etternavn,epost,fødselsdato,kjønn,studium]]
        studentnr=studenter.readline()
    studenter.close()

    print("Velg utskrift ut ifra liste under:")
    print("1: Skriv ut hele lista")
    print("2: Skriv ut fornavn, etternavn og fødselsdato")
    print("3: Skriv ut kun kvinnelige studenter")
    print("4: Skriv ut kun studenter ved Bach IT og IS")

    valg=int(input("Velg nummer på ønsket utskrift (1/2/3/4): "))

    if valg==1:
        print()
        print("Hele lista:")
        print()
        for x in range (0,len(liste),1):
            print("Studentnr:",liste[x][0],"Fornavn:",liste[x][1],"Etternavn:",liste[x][2],"E-postadresse:",liste[x][3],"Fødselsdato",liste[x][4],"Kjønn:",liste[x][5],"studium:",liste[x][6])
        
    
    if valg==2:
        print()
        print("Fornavn, Etternavn og Fødselsdato:")
        print()
        for y in range (0,len(liste),1):
            print(liste[y][1],liste[y][2],liste[y][4])
        

    if valg==3:
        print()
        print("Bare kvinner:")
        print()
        for n in range (0,len(liste),1):
            if liste[n][5]=="K":
                print(liste[n][1],liste[n][2],liste[n][3])
        

    if valg==4:
        print()
        print("Studenter ved Bach IT og IS:")
        print()
        for m in range (0,len(liste),1):
            if liste[m][6]=="Bach IT og IS":
                print(liste[m][0],liste[m][1],liste[m][2],liste[m][5])
        


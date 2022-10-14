import sys

liste={}

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

        liste[studentnr]={"Fornavn":fornavn,"Etternavn":etternavn,"Epost":epost,"Fødselsdato":fødselsdato,"Kjønn":kjønn,"Studium":studium}
        studentnr=studenter.readline()
    studenter.close()

    #print("Kontaktlista mi er:",liste)

    listelengde=len(liste)
    #print("Listelengde:",listelengde)

    antallKvinner=0
    antallIT=0
    antallØkadm=0

    for x in liste:
        if liste[x]["Kjønn"].upper()=="K":
            antallKvinner+=1
        if liste[x]["Studium"].upper()=="BACH IT OG IS":
            antallIT+=1
        if liste[x]["Studium"].upper()=="BACH ØKADM":
            antallØkadm+=1
    
    print("Antall kvinner:",antallKvinner)
    print()
    print("Antall IT studenter:",antallIT)
    print()
    print("Antall Økonomi studenter:",antallØkadm)



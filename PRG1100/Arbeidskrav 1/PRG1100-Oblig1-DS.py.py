#Importerer sys til bruk på feilhåndtering
import sys

#Definere programmet innlesning(): for lesing fra fil til 2-dimensjonal liste
def innlesing():

    #Definerer tom liste
    vare=[]

    #Feilhåndtering for manglende fil
    try:
        #Forsøker å åpne filen
        varefil=open("Vare.txt","r",encoding=("UTF-8"))
    except IOError:
        #Dersom filen ikke eksisterer printes følgende
        print("Filen finnes ikke i målet")
    else:

        #Leser første linje i vare.txt filen og definerer denne som varenr
        varenr=varefil.readline()

        #Så lenge varenr ikke er tom fortsetter løkken
        while varenr !="":
            #fjerner new line merket på varenr
            varenr=varenr.rstrip("\n")
            #Definerer betegnelse som neste linje i filen og fjerner new line merket
            betegnelse=varefil.readline().rstrip("\n")
            #Definerer pris som neste linje i filen og fjerner new line merket
            pris=varefil.readline().rstrip("\n")
            #Definerer kategori som neste linje i filen og fjerner new line merket
            kategori=varefil.readline().rstrip("\n")
            #Definerer hylle som neste linje i filen og fjerner new line merket
            hylle=varefil.readline().rstrip("\n")

            #Skriver varenr, betegnelse, pris, kategori og hylle over til 2-dimensjona fil
            vare+=[[varenr,betegnelse,pris,kategori,hylle]]

            #leser neste linje i filen og definerer denne som varenr.
            varenr=varefil.readline()

        return vare

#Definerer programmet hylleplassering(): for printing av alle varer og hylleplasser med parameteroverføring
def hylleplassering(listeVarer):

    #Definerer variabel for while-løkke
    fortsette="j"

    #While-løkke som tillater bruker å gjennomføre ny print uten å måtte gå via menyen på nytt
    while fortsette=="j":
        
        #Definerer liste for hylleplass
        listeHylleplass=[]
        
        #For-løkke for å gå gjennom hele listen rad for rad
        for x in range (len(listeVarer)):
            #skriver hver del av listen i listen over til ny liste
            listeHylleplass+=[[listeVarer[x][1],listeVarer[x][4]]]

        #Printer resultatet av for-løkken
        print("Fullstending liste over alle hylleplasserte varer:")
        print(listeHylleplass)
        print()

        #Spør bruker om de ønsker å gjennomføre ny utskrift
        fortsette=input("Ønsker du å foreta utskift på nytt? (j/n): ")
        print()

#Definerer programmet hylleplasseringNull(): for printing av alle varer uten hylleplassering med parameteroverføring
def hylleplasseringNull(listeVarer):

    #Definerer variabel for while-løkke
    fortsette="j"

    #While-løkke som tillater at bruker kan gjennomføre flere utskrifter uten å måtte gå via hovedmenyen.
    while fortsette=="j":

        #Definerer funnet=False
        funnet=False
        #Definerer listen listeMangerHylle
        listeManglerHylle=[]
        
        #For-løkke som går gjennom 2-dimensjonal liste rad for rad
        for n in range (len(listeVarer)):
            #Dersom varen i listen i listen har "NULL" merket som verdi på possisjon for hylle, skrives varen over i ny liste
            if listeVarer[n][4].upper()=="NULL":
                #Definerer funnet=True dersom det eksisterer varer uten hylleplassering
                funnet=True
                #Skriver varen over til ny 2-dimensjonal liste
                listeManglerHylle+=[[listeVarer[n][0],listeVarer[n][1],listeVarer[n][2],listeVarer[n][3],listeVarer[n][4]]]
        
        #Dersom vare uten hylle er funnet;
        if funnet==True:
            #Print resultatet If testen
            print("Fullestending liste over alle varer uten hylleplassering:")
            print(listeManglerHylle)
            print()
        #Dersom ingen varer uten hylleplassering er funnet;
        else:
            #Print informasjon om dette til bruker
            print("Ingen varer mangler hylleplassering")
            print()
        
        #Spør om bruker ønsker å gjennomføre nytt søk
        fortsette=input("Ønsker du å foreta nytt søk? (j/n): ")
        print()

#Definerer programmet varesokForbokstav(): for søk og printing av varer filtrert på forbokstav i varenavn, med parameteroverføring
def varesokForbokstav(listeVarer):

    #Definerer variabel for while-løkke
    fortsette="j"
    #While-løkke som tillater bruker å foreta flere søk uten å måtte gå via hovedmenyen
    while fortsette=="j":

        #Definerer funnet=False
        funnet=False
        #Definerer resutlaterForbokstav som ny liste
        resultatForbokstav=[]
        
        #Ber bruker oppgi forbokstav de ønsker å søke på
        sokForbokstav=input("Oppgi forbokstaven på varen du leter etter: ")

        #For-løkke som går gjennom 2-dimensjonal liste rad for rad
        for i in range (len(listeVarer)):
            #Dersom første bokstav i første ordet i gjeldende liste, lest som stor bokstav, tilsvarer bokstav søkt etter, lest som stor bokstav;
            if listeVarer[i][1][0:1].upper()==sokForbokstav.upper():
                #Definer funnet=True
                funnet=True
                #Skriv varen inn i ny liste
                resultatForbokstav+=[[listeVarer[i][0],listeVarer[i][1],listeVarer[i][2],listeVarer[i][3],listeVarer[i][4]]]
        #Dersom vare med korrekt forbokstav er funnet;
        if funnet==True:
            #Print resultatet av søket
            print("Fullstending liste over alle varer med ønsket forbokstav")
            print(resultatForbokstav)
            print()
        #Dersom ingen vare med korrekt forbokstav er funnet;
        else:
            #Print informasjon om dette til bruker
            print("Ingen varer med denne forbokstaven funnet")
            print()
        
        #Spør om bruker ønsker å foreta nytt søk
        fortsette=input("Ønsker du å foreta nytt søk? (j/n): ")
        print()

#Definerer programmet kategorisok(): for søk og printing av varer filteret på kategori, med parameteroverføring
def kategorisok(listeVarer):
    
    fortsette="j"
    while fortsette=="j":

        kategori=input("Oppgi kategorien du ønsker å søke etter: ")

        listeKatergorisok=[]
        funnet=False

        for m in range (len(listeVarer)):
            if listeVarer[m][3].upper()==kategori.upper():
                funnet=True
                listeKatergorisok+=[[listeVarer[m][0],listeVarer[m][1],listeVarer[m][2],listeVarer[m][3],listeVarer[m][4]]]
            
        if funnet==True:
            print("Kategori",kategori,"har",len(listeKatergorisok),"antall varer")
            print("Fullstending liste over alle varer innenfor ønsket kategori:")
            print(listeKatergorisok)
            print()
        else:
            print("Ingen varer i ønsket kategori funnet")
            print()
        
        fortsette=input("Ønsker du å foreta nytt søk? (j/n): ")
        print()

#Definerer programmet prisintervall(): for søk og printing av varer med pris mellom 100,- og 200,-, med parameteroverføring
def prisintervall(listeVarer):
    
    #Definerer variabel for while-løkke
    fortsette="j"
    #While-løkke som tillater bruker å gjennomføre nytt søk uten å gå via hovedmenyen
    while fortsette=="j":

        #Defienrer funnet=False
        funnet=False
        #Definerer ny liste prisliste
        prisliste=[]

        #Forløkke som går gjennom 2-dimensjonal liste rad for rad
        for d in range (len(listeVarer)):
            #Dersom tallet i rad som tilsvarer pris er større enn eller lik 100 og mindre enn eller lik 200;
            if int(listeVarer[d][2])>=100 and int(listeVarer[d][2])<=200:
                #Defienr funnet=True
                funnet=True
                #Skriv vare over til ny liste
                prisliste+=[[listeVarer[d][0],listeVarer[d][1],listeVarer[d][2],listeVarer[d][3],listeVarer[d][4]]]

        #Dersom vare i ønsket intervall er funnet;
        if funnet==True:
            #Print resultatet av søket
            print("Fullstendig liste over alle varer med verdi mellom 100,- og 200,-")
            print(prisliste)
            print()
        #Dersom ingen varer i ønsket intervall ble funnet;
        else:
            #Print informasjon om dette til bruker
            print("Ingen varer mellom 100,- og 200,- funnet")
            print()
        
        #Spør om kunde ønsker å foreta nytt søk
        fortsette=input("Ønsker du å forta nytt søk? (j/n): ")
        print()

#Definerer programmet listesortering(): for bobblesortering av liste og skriving over til ny sortert fil, med parameteroverføring
def listesortering(listeVarer):

    #Definerer variabel for kontroll om bytting ble gjennomført ved forrige gjennomgang av while-løkke
    bytte=True
    #Definerer stoppmerket
    stoppmerke=1

    #While-løkke som kjører frem til ingen bytter har blitt gjennomført
    while bytte==True:
        #Definere bytte=False
        bytte=False

        #For-løkke som går gjennom 2-dimensjonal liste rad for rad med stoppmerket som øker for hver gjennomkjøring
        for b in range(len(listeVarer)-stoppmerke):
            #Dersom varenavn i gjeldende liste er større enn varenavn i neste liste;
            if listeVarer[b][1]>listeVarer[b+1][1]:
                #Definer bytte=True
                bytte=True
                #Skriv vare over tiu temp variabel
                temp=listeVarer[b]
                #Definer gjeldene liste som neste liste
                listeVarer[b]=listeVarer[b+1]
                #Definere neste liste som liste i temp
                listeVarer[b+1]=temp
        
        #Flytt stoppmerke ett steg frem
        stoppmerke+=1

    #Åpner ny fil i write
    sortertfil=open("SortertVare.txt","w",encoding=("UTF-8"))

    #For løkke som går gjennom ny liste rad for rad
    for y in range (len(listeVarer)):
        #Skriver hver rad over til ny fil med new line merket
        sortertfil.write(listeVarer[y][0]+"\n"+listeVarer[y][1]+"\n"+listeVarer[y][2]+"\n"+listeVarer[y][3]+"\n"+listeVarer[y][4]+"\n")
    #Stenger sortert fil
    sortertfil.close()

    #Informerer bruker om at sortering av fil er gjennomført
    print("Sortert liste av varer lagret som 'SortertVare.txt'")
    print()

#Definerer main(): for menystruktur
def main():

    #Setter endret=True for å kontrollere innlesning til ny liste
    endret=True
    #Definerer variabel for while løkke på menyen
    fortsette=True

    #While-løkke kjører til bruker ikke ønsker å kjøre programmet lenger.
    while fortsette==True:
        
        #Dersom listen har blitt endret av program 6, skal innlesning kalles på nytt for å skrive ny liste fra fil.
        if endret==True:
        
            vareliste=innlesing()
            #Etter skriving til ny liste skal endret settes lik False for å unngå unødvendig overskriving av listen.
            endret=False

        #Beskrivelse av menysystemet
        print("Vennligst velg funksjon fra listen;")
        print("----------------------------------------------------------------------------------")
        print("1: Skriv ut liste av hver vare og varens hylleplassering")
        print("2: Skriv ut liste med alle varer uten hylleplassering")
        print("3: Søk etter varenavn på forbokstav")
        print("4: Søk etter varer på kategori")
        print("5: Skriv ut liste over alle med pris mellom 100,- og 200,-")
        print("6: Sorter vareliste og lagre som ny liste 'SortertVare.txt' ")
        print("9: Avslutt")
        print("----------------------------------------------------------------------------------")

        #Be bruker definerer funksjon i programmet de ønsker å benytte
        valg=input("Skriv inn tallet til funksjonen du ønsker å benytte: ")
        print()

        #If statements som informerer bruker om hvilken funksjon de har valgt og som kaller den ønskede funksjonen med parameteroverføring.
        if valg=="1":
            print("Du har valgt funksjon nr. 1: Hylleplassering")
            print()
            hylleplassering(vareliste)
        elif valg=="2":
            print("Du har valgt funksjon nr. 2: Ikke hylleplassert")
            print()
            hylleplasseringNull(vareliste)
        elif valg=="3":
            print("Du har valgt funksjon nr. 3: Søk på forbokstav")
            print()
            varesokForbokstav(vareliste)
        elif valg=="4":
            print("Du har valg funksjon nr. 4: Søk på kategori")
            print()
            kategorisok(vareliste)
        elif valg=="5":
            print("Du har valg funksjon nr. 5: Prisliste 100,- til 200,-")
            print()
            prisintervall(vareliste)
        elif valg=="6":
            print("Du har valg funksjon nr. 6: Sortering")
            print()
            listesortering(vareliste)
            #Setter endret=True for å lese inn ny liste fra fil uten sortering
            endret=True
        elif valg=="9":
            fortsette=False
        #Fail safe dersom bruker taster inn tall i menyen som ikke tilhører en funksjon i programmet.
        else:
            print("Tallet",valg,"er ikke en funksjon i dette programmet")
            print()

#Tilkaller funksjonen main():
main()
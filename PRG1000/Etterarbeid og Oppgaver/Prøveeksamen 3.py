import os

def registrer_ny_kunde():
    
    reglokke="j"
    
    while reglokke=="j":
        
        idKontroll="j"
        
        while idKontroll=="j":
            
            kunde=open("kunde.txt","r")
            
            mobilnr=input("Oppgi mobilnummer: ")
            
            kundeKontroll=kunde.readline()
            
            duplikatKontroll=True
            
            while kundeKontroll!="":
                
                if mobilnr==kundeKontroll.rstrip("\n"):
                    
                    print("Kunde er allerede Registrert")
                    
                    idKontroll=input("Ønsker du å prøve et annet tlf nummer? (j/n): ")
                    
                    duplikatKontroll=False
                    
                    if idKontroll=="n":
                        
                        reglokke="n"
                        
                kundeKontroll=kunde.readline()
                
            if duplikatKontroll==True:
                idKontroll="n"
                kunde.close()
                kunde=open("kunde.txt","a")
                fornavn=input("Oppgi fornavn: ")
                etternavn=input("Oppgi etternavn: ")
                betalingskortnr=input("Oppgi betalingskortnr: ")
                kunde.write(mobilnr+"\n"+fornavn+"\n"+etternavn+"\n"+betalingskortnr+"\n")
                kunde.close()
                print()
                print("Registering fullført")
                reglokke=input("Ønsker du å legge inn ny kunde? (j/n): ")

def registrer_ny_hund():
    reglokke="j"
    while reglokke=="j":
        idKontroll="j"
        while idKontroll=="j":
            
            hund=open("Hund.txt","r")
            
            hundeId=input("Oppgi HundeID: ")
            
            hundeKontroll=hund.readline()
            
            duplikatKontroll=True
            
            while hundeKontroll!="":
                if hundeId==hundeKontroll.rstrip("\n"):
                    print("Hund er allerede Registrert")
                    idKontroll=input("Ønsker du å prøve et annet ID nummer? (j/n): ")
                    duplikatKontroll=False
                    if idKontroll=="n":
                        reglokke="n"
                hundeKontroll=hund.readline()
                
            if duplikatKontroll==True:
                idKontroll="n"
                hund.close()
                hund=open("hund.txt","a")
                hundenavn=input("Oppgi hundenavn: ")
                rase=input("Oppgi rase: ")
                mobilnr=input("Oppgi eiers mobilnummer: ")
                startDato=input("Oppgi startdato: ")
                hund.write(hundeId+"\n"+hundenavn+"\n"+rase+"\n"+mobilnr+"\n"+startDato+"\n")
                hund.close()
                print()
                print("Registering fullført")
                reglokke=input("Ønsker du å legge inn ny hund? (j/n): ")

def slett_kunde():
    nyttSok="j"
    while nyttSok=="j":
        mobilnr=input("Skriv inn telefonnummer til kunde: ")
        funnet=False
        kundeSletting=open("hund.txt","r")
        kontroll=kundeSletting.readline()
        while kontroll!="":
            if kontroll.rstrip("\n")==mobilnr:
                funnet=True
            kontroll=kundeSletting.readline()
        if funnet==False:
            print("Kunde har ingen hunder registert på seg")
            print("Ønsker du å slette kunde?")
            slette=input("(j/n:) ")
            if slette=="j":
                kundeSletting.close()
                kundeSletting=open("kunde.txt","r")
                tempfil=open("temp.txt","w")
                mobilnummer=kundeSletting.readline()
                while mobilnummer!="":
                    fornavn=kundeSletting.readline()
                    etternavn=kundeSletting.readline()
                    betalingskortnr=kundeSletting.readline()
                    if mobilnummer.rstrip("\n")!=mobilnr:
                        tempfil.write(mobilnummer+fornavn+etternavn+betalingskortnr)
                    mobilnummer=kundeSletting.readline()
                tempfil.close()
                kundeSletting.close()
                os.remove("kunde.txt")
                os.rename("temp.txt","kunde.txt")
                print()
                print("Kunde slettet")
                print()
                print("Ønsker du å slette en ny kunde?")
                nyttSok=input("(j/n): ")
        else:
            print("Kunde har hund registert på seg og kan derfor ikke slettes")
            print()
            print("Ønsker du å søke opp en annen kunde?")
            nyttSok=input("(j/n): ")

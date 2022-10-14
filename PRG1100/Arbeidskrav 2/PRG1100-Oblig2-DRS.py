from tkinter.ttk import Combobox
import mysql.connector
from tkinter import *


mindatabase=mysql.connector.connect(host="localhost",port="3306",user="Eksamenssjef",passwd="oblig2022",db="oblig2022")

#Registrering av nye studenter
def studentregistreringWindow2():

    #Kode for tømming av entryfelt etter lagring
    def entryTomming():

        fnavn.set("")
        enavn.set("")
        epst.set("")
        tlfnr.set("")
    
    #Kode for registrering 
    def registrerStudent():

        studentnr=studnr.get()
        fornavn=fnavn.get()
        etternavn=enavn.get()
        epost=epst.get()
        telefonnr=tlfnr.get()

        registrerMarkor=mindatabase.cursor()

        registrerStudent=("INSERT INTO Student"
                        "(Studentnr, Fornavn, Etternavn, Epost, Telefon)"
                        "VALUES(%s,%s,%s,%s,%s)")
        studentdata=(studentnr,fornavn,etternavn,epost,telefonnr)

        registrerMarkor.execute(registrerStudent,studentdata)
        mindatabase.commit()
        registrerMarkor.close()

        txtboks.config(state=NORMAL)
        txtboks.delete("1.0","end")
        txtboks.insert("1.0","Ny student lagret med studentnr:"+studentnr)
        txtboks.config(state=DISABLED)

        nyttStudentnr()
        entryTomming()

    #Kode for automatisk genererering av nytt studentnummer
    def nyttStudentnr():
    
        studnrmarkor=mindatabase.cursor()
        studnrmarkor.execute("SELECT MAX(Studentnr) FROM Student")

        hoyestStudnr=[]
        for row in studnrmarkor:
            hoyestStudnr+=[row[0]]

        studnrmarkor.close()
        
        nyttStudentnr=int(hoyestStudnr[0])+1
        studnr.set(nyttStudentnr)
    
    window2=Toplevel()
    window2.title("Studentregistrering")

    #Variabler
    studnr=StringVar()
    fnavn=StringVar()
    enavn=StringVar()
    epst=StringVar()
    tlfnr=StringVar()

    #Studentnr
    nyttStudentnr()
    lblStudentnr=Label(window2,text="Studentnr:")
    lblStudentnr.grid(row=0,column=0,padx=5,pady=5,sticky=E)
    entStudnr=Entry(window2,state="readonly",width=6,textvariable=studnr)
    entStudnr.grid(row=0,column=1,padx=5,pady=5,sticky=W)

    #Fornavn
    lblFnavn=Label(window2,text="Fornavn:")
    lblFnavn.grid(row=1,column=0,padx=5,pady=5,sticky=E)
    entFnavn=Entry(window2,width=30,textvariable=fnavn)
    entFnavn.grid(row=1,column=1,padx=5,pady=5,sticky=W)

    #Etternavn
    lblEnavn=Label(window2,text="Etternavn:")
    lblEnavn.grid(row=2,column=0,padx=5,pady=5,sticky=E)
    entEnavn=Entry(window2,width=20,textvariable=enavn)
    entEnavn.grid(row=2,column=1,padx=5,pady=5,sticky=W)

    #Epost
    lblEpst=Label(window2,text="Epost:")
    lblEpst.grid(row=3,column=0,padx=5,pady=5,sticky=E)
    entEpst=Entry(window2,width=40,textvariable=epst)
    entEpst.grid(row=3,column=1,padx=5,pady=5,sticky=W)

    #Telefonnr
    lbltlfnr=Label(window2,text="Telefonnr:")
    lbltlfnr.grid(row=4,column=0,padx=5,pady=5,sticky=E)
    entTlfnr=Entry(window2,width=8,textvariable=tlfnr)
    entTlfnr.grid(row=4,column=1,padx=5,pady=5,sticky=W)

    #tekstboks
    txtboks=Text(window2,width=40,height=1)
    txtboks.grid(row=5,column=1,columnspan=2,padx=5,pady=5)

    #knapper
    btnLagre=Button(window2,text="Lagre",command=registrerStudent)
    btnLagre.grid(row=6,column=2,padx=5,pady=5,sticky=E)
    btnTilbake=Button(window2,text="Tilbake",command=window2.destroy)
    btnTilbake.grid(row=6,column=3,padx=5,pady=5,sticky=E)

#Redigering av en eksisterende student
def studentredigeringWindow3():
    
    #Hente informasjon fra database ved curselection
    def hentInfo():

        slettStudnr=studnr.get()

        infomarkor=mindatabase.cursor()
        infomarkor.execute("SELECT * FROM Student")

        for row in infomarkor:
            if slettStudnr==row[0]:
                studnr.set(row[0])
                fornavn.set(row[1])
                etternavn.set(row[2])
                epost.set(row[3])
                telefonnr.set(row[4])

        infomarkor.close()

        txtboks.delete("1.0","end")

    #Lagre endringer til database
    def lagreEndringer():
        endringsmarkor=mindatabase.cursor()
        
        studnrEndring=studnr.get()
        enavnEndring=etternavn.get()
        epostEndring=epost.get()
        tlfnrEndring=telefonnr.get()

        endre=("UPDATE Student SET Etternavn=%s, Epost=%s, Telefon=%s WHERE Studentnr=%s")
        endreData=(enavnEndring, epostEndring, tlfnrEndring, studnrEndring)

        try:
            endringsmarkor.execute(endre,endreData)
        except:
            txtboks.config(state=NORMAL)
            txtboks.delete("1.0","end")
            txtboks.insert("1.0","Student kan ikke redigeres")
            txtboks.config(state=DISABLED)
            mindatabase.commit()
        else:
            endringsmarkor.close()
            txtboks.config(state=NORMAL)
            txtboks.delete("1.0","end")
            txtboks.insert("1.0","Student endret")
            txtboks.config(state=DISABLED)

    window3=Toplevel()
    window3.title("Studentregistrering")

    #Variabler
    studnr=StringVar()
    fornavn=StringVar()
    etternavn=StringVar()
    epost=StringVar()
    telefonnr=StringVar()

    #studentnr
    lblStudnr=Label(window3,text="Studentnr:")
    lblStudnr.grid(row=0,column=3,padx=5,pady=5,sticky=E)
    entStudnr=Entry(window3,width=6,textvariable=studnr)
    entStudnr.grid(row=0,column=4,padx=5,pady=5,sticky=W)

    #Søkeknapp
    btnSokStudent=Button(window3,text="Søk",command=hentInfo)
    btnSokStudent.grid(row=1,column=4,padx=5,pady=5,sticky=W)

    #Fornavn
    lblFornavn=Label(window3,text="Fornavn:")
    lblFornavn.grid(row=2,column=3,padx=5,pady=5,sticky=E)
    entFornavn=Entry(window3,width=30,state="readonly",textvariable=fornavn)
    entFornavn.grid(row=2,column=4,padx=5,pady=5,sticky=W)

    #Etternavn
    lblEtternavn=Label(window3,text="Etternavn:")
    lblEtternavn.grid(row=3,column=3,padx=5,pady=5,sticky=E)
    entEtternavn=Entry(window3,width=20,textvariable=etternavn)
    entEtternavn.grid(row=3,column=4,padx=5,pady=5,sticky=W)

    #Epost
    lblEpost=Label(window3,text="Epost:")
    lblEpost.grid(row=3,column=3,padx=5,pady=5,sticky=E)
    entEpost=Entry(window3,width=40,textvariable=epost)
    entEpost.grid(row=3,column=4,padx=5,pady=5,sticky=W)

    #Telefonnr
    lblTelefonnr=Label(window3,text="Telefonnr:")
    lblTelefonnr.grid(row=4,column=3,padx=5,pady=5,sticky=E)
    entTelefonnr=Entry(window3,width=8,textvariable=telefonnr)
    entTelefonnr.grid(row=4,column=4,padx=5,pady=5,sticky=W)

    #tekstboks
    txtboks=Text(window3,width=21,height=1)
    txtboks.grid(row=5,column=4,columnspan=2,padx=5,pady=5,sticky=W)

    #knapper
    btnLagre=Button(window3,text="Lagre",command=lagreEndringer)
    btnLagre.grid(row=6,column=5,padx=5,pady=5,sticky=E)
    btnTilbake=Button(window3,text="Tilbake",command=window3.destroy)
    btnTilbake.grid(row=6,column=6,padx=5,pady=5,sticky=E)

#Sletting av en eksisterende student
def studentslettingWindow4():
    
    #Sletting av en student fra database
    def slettStudent():
        sletteMarkor=mindatabase.cursor()

        slettVare=("DELETE FROM Student WHERE Studentnr=%s")
        slettData=(studnr.get(),)
        try:
            sletteMarkor.execute(slettVare, slettData)
        except:
            txtbox.config(state=NORMAL)
            txtbox.delete("1.0","end")
            txtbox.insert("1.0","Student kan ikke slettes")
            txtbox.config(state=DISABLED)
        else:
            mindatabase.commit()
            txtbox.config(state=NORMAL)
            txtbox.delete("1.0","end")
            txtbox.insert("1.0","Student slettet")
            txtbox.config(state=DISABLED)
        
        sletteMarkor.close()
        studnr.set("")
        fornavn.set("")
        etternavn.set("")
        epost.set("")
        tlfnr.set("")

    #Hente informasjon fra database
    def hentInfo():

        stdnr=studnr.get()

        infomarkor=mindatabase.cursor()
        infomarkor.execute("SELECT * FROM Student")

        for row in infomarkor:
            if stdnr==row[0]:
                fornavn.set(row[1])
                etternavn.set(row[2])
                epost.set(row[3])
                tlfnr.set(row[4])

        infomarkor.close()

    window4=Toplevel()
    window4.title("Studentsletting")

    #Variabler
    studnr=StringVar()
    fornavn=StringVar()
    etternavn=StringVar()
    epost=StringVar()
    tlfnr=StringVar()

    #Studentnr
    lblStudnr=Label(window4,text="Legg inn studentnr:")
    lblStudnr.grid(row=0,column=0,padx=5,pady=5,sticky=E)
    entStudnr=Entry(window4,width=6,textvariable=studnr)
    entStudnr.grid(row=0,column=1,padx=5,pady=5,sticky=W)

    #Søkeknapp
    btnSok=Button(window4,text="Søk",command=hentInfo)
    btnSok.grid(row=1,column=1,padx=5,pady=5,sticky=W)

    #Fornavn
    lblFornavn=Label(window4,text="Fornavn:")
    lblFornavn.grid(row=2,column=0,padx=5,pady=5,sticky=E)
    entFornavn=Entry(window4,width=30,state="readonly",textvariable=fornavn)
    entFornavn.grid(row=2,column=1,padx=5,pady=5,sticky=W)

    #Etternavn
    lblEtternavn=Label(window4,text="Etternavn:")
    lblEtternavn.grid(row=3,column=0,padx=5,pady=5,sticky=E)
    entEtternavn=Entry(window4,width=20,state="readonly",textvariable=etternavn)
    entEtternavn.grid(row=3,column=1,padx=5,pady=5,sticky=W)

    #Epost
    lblEpost=Label(window4,text="Epost adresse:")
    lblEpost.grid(row=4,column=0,padx=5,pady=5,sticky=E)
    entEpost=Entry(window4,width=40,state="readonly",textvariable=epost)
    entEpost.grid(row=4,column=1,padx=5,pady=5,sticky=W)

    #Telefonnr
    lbltlf=Label(window4,text="Telefonnr:")
    lbltlf.grid(row=5,column=0,padx=5,pady=5,sticky=E)
    enttlf=Entry(window4,width=8,state="readonly",textvariable=tlfnr)
    enttlf.grid(row=5,column=1,padx=5,pady=5,sticky=W)

    #Textbox
    txtbox=Text(window4,width=30,height=1)
    txtbox.grid(row=6,column=1,padx=5,pady=5,sticky=W)

    #knapper
    btnSlett=Button(window4,text="Slett valgt student",command=slettStudent)
    btnSlett.grid(row=7,column=2,padx=5,pady=5,sticky=W)
    btnTilbake=Button(window4,text="Tilbake",command=window4.destroy)
    btnTilbake.grid(row=7,column=3,padx=5,pady=5,sticky=E)

#Registrering av ny eksamen
def eksamensregistreringWindow5():

    #Finne ledig rom på valgt dato
    def finnLedigRom():
        
        rommarkor=mindatabase.cursor()
        
        rom=("SELECT Romnr FROM Rom WHERE NOT EXISTS (SELECT * FROM Eksamen WHERE Dato=%s AND Rom.Romnr=Eksamen.Romnr)")
        valgtDato=(dato.get(),)
        rommarkor.execute(rom,valgtDato)

        romliste=[]

        for row in rommarkor:
            romliste+=[row[0]]
        
        romlisteInnhold.set(romliste)
        rommarkor.close()

    #Hente informasjon fra database om valgt rom
    def hentInfoValgtRom(event):
        valg=listeRom.get(listeRom.curselection())

        valgmarkor=mindatabase.cursor()
        valgmarkor.execute("SELECT * From Rom")

        for i in valgmarkor:
            if i[0]==valg:
                romvalg.set(i[0])
                antallPlasser.set(i[1])

        valgmarkor.close()

    #Lagre registrering til database
    def lagreRegistrering():
        
        regDato=dato.get()
        regEmne=comboEmnevalg.get()
        regRom=romvalg.get()

        registreringsmarkor=mindatabase.cursor()
        registrering=("INSERT INTO Eksamen"
                    "(Emnekode, Dato, Romnr)"
                    "VALUES(%s,%s,%s)")
        info=(regEmne,regDato,regRom)
        registreringsmarkor.execute(registrering,info)
        mindatabase.commit()
        registreringsmarkor.close()

        finnLedigRom()

    #Hente emnekoder fra database for combobox
    emnemarkor=mindatabase.cursor()
    emnemarkor.execute("SELECT Emnekode FROM Emne")
    emneliste=[]
    for i in emnemarkor:
        emneliste+=[i[0]]
    emnemarkor.close()

    window5=Toplevel()
    window5.title("Eksamensregistrering")

    #Variabler
    romlisteInnhold=StringVar()
    dato=StringVar()
    emnevalg=StringVar()
    romvalg=StringVar()
    antallPlasser=StringVar()

    #Listebox
    yScroll=Scrollbar(window5,orient=VERTICAL)
    yScroll.grid(row=0,column=2,rowspan=10,padx=(0,100),pady=5,sticky=NS)
    listeRom=Listbox(window5,width=20,height=10,listvariable=romlisteInnhold,yscrollcommand=yScroll.set)
    listeRom.grid(row=0,column=1,rowspan=10,padx=(100,0),pady=5,sticky=E)
    yScroll["command"]=listeRom.yview
    listeRom.bind("<<ListboxSelect>>",hentInfoValgtRom)

    #Datofilter
    lblDato=Label(window5,text="Dato for eksamen:")
    lblDato.grid(row=1,column=3,padx=5,pady=5,sticky=E)
    entDato=Entry(window5,width=8,textvariable=dato)
    entDato.grid(row=1,column=4,padx=5,pady=5,sticky=W)
    btnFinnLedigRom=Button(window5,text="Finn ledig rom",command=finnLedigRom)
    btnFinnLedigRom.grid(row=2,column=3,padx=5,pady=5,sticky=E)
    
    #Combobox for emnevalg   
    lblEmnevalg=Label(window5,text="Velg Emne")
    lblEmnevalg.grid(row=0,column=3,padx=5,pady=5,sticky=E)
    comboEmnevalg=Combobox(window5,width=8,values=emneliste)
    comboEmnevalg.grid(row=0,column=4,padx=5,pady=5,sticky=W)
    comboEmnevalg.state(["readonly"])
    comboEmnevalg.current(0)
    emnevalg.set(comboEmnevalg.current())

    #Antall Plasser
    lblAntallPlasser=Label(window5,text="Antall Plasser")
    lblAntallPlasser.grid(row=3,column=3,padx=5,pady=5,sticky=E)
    entAntallPlasser=Entry(window5,width=3,state="readonly",textvariable=antallPlasser)
    entAntallPlasser.grid(row=3,column=4,padx=5,pady=5,sticky=W)

    #Knapper
    btnLagre=Button(window5,text="Lagre",command=lagreRegistrering)
    btnLagre.grid(row=11,column=3,padx=5,pady=5,sticky=E)
    btnTilbake=Button(window5,text="Tilbake",command=window5.destroy)
    btnTilbake.grid(row=11,column=4,padx=5,pady=5,sticky=E)

#Redigering av eksisterende eksamen
def eksamensredigeringWindow6():
    
    #Lagre endringer til database
    def lagreEndringer():
        endreEmnekode=emnekode.get()
        endreDato=dato.get()
        endreRomnr=romnr.get()

        årGet=str(endreDato[:4])
        manedGet=str(endreDato[5:7])
        dagGet=str(endreDato[8:10])
        datoFraGet=årGet+manedGet+dagGet

        kontrollmarkor=mindatabase.cursor()
        endremarkor=mindatabase.cursor()
        kontrollmarkor.execute("SELECT * FROM Eksamen")

        eksamensliste=[]
        for row in kontrollmarkor:
            eksamensliste+=[[row[0],str(row[1]),row[2]]]
        
        duplikat=False
        for i in range(0,len(eksamensliste)):
            if eksamensliste[i]==[endreEmnekode,endreDato,endreRomnr]:
                duplikat=True
        if duplikat==False:
            oppdatering=("UPDATE Eksamen SET Romnr=%s WHERE Emnekode=%s AND Dato=%s")
            endreData=(endreRomnr,endreEmnekode,datoFraGet)
            endremarkor.execute(oppdatering,endreData)
            mindatabase.commit()
            txtboks.config(state=NORMAL)
            txtboks.delete("1.0","end")
            txtboks.insert("1.0","Eksamen endret")
            txtboks.config(state=DISABLED)
        else:
            txtboks.config(state=NORMAL)
            txtboks.delete("1.0","end")
            txtboks.insert("1.0","Rom allerede i bruk")
            txtboks.config(state=DISABLED)

        endremarkor.close()
        kontrollmarkor.close()

        lesTilListe()

    #Leser fra database til liste for listeboks
    def lesTilListe():
        
        eksamensmarkor=mindatabase.cursor()
        eksamensmarkor.execute("SELECT * FROM Eksamen")
        eksamensliste=[]
        for row in eksamensmarkor:
            eksamensliste+=[[row[0],row[1],row[2]]]
        eksamen.set(eksamensliste)
        eksamensmarkor.close()

    #Henter informasjon om valg eksamen fra listeboks
    def hentEksamensinfo(event):
        valg=eksamensliste.get(eksamensliste.curselection())
        hentEmnekode=valg[0]
        hentRomnr=valg[2]
        
        testmarkor=mindatabase.cursor()

        årValg=str(valg[1][:4])
        manedValg=str(valg[1][5:7])
        dagValg=str(valg[1][8:10])
        datoFraValg=årValg+manedValg+dagValg

        seleksjonEksamen=("SELECT * FROM Eksamen WHERE Dato=%s AND Emnekode=%s AND Romnr=%s")
        datoData=(datoFraValg,hentEmnekode,hentRomnr)

        testmarkor.execute(seleksjonEksamen,datoData)

        for i in testmarkor:
            emnekode.set(i[0])
            dato.set(i[1])
            romnr.set(i[2])

        testmarkor.close()
        

    window6=Toplevel()
    window6.title("Eksamensendring")

    #Variabler
    eksamen=StringVar()
    dato=StringVar()
    romnr=StringVar()
    emnekode=StringVar()

    #Listeboks
    lesTilListe()
    yScroll=Scrollbar(window6,orient=VERTICAL)
    yScroll.grid(row=0,column=2,rowspan=10,padx=(0,100),pady=5,sticky=NS)
    eksamensliste=Listbox(window6,width=25,height=10,listvariable=eksamen,yscrollcommand=yScroll.set)
    eksamensliste.grid(row=0,column=1,rowspan=10,padx=(100,0),pady=5,sticky=E)
    yScroll["command"]=eksamensliste.yview
    eksamensliste.bind("<<ListboxSelect>>",hentEksamensinfo)

    #Emnekode
    lblEmnekode=Label(window6,text="Emnekode:")
    lblEmnekode.grid(row=0,column=3,padx=5,pady=5,sticky=E)
    entEmnekode=Entry(window6,width=8,state="readonly",textvariable=emnekode)
    entEmnekode.grid(row=0,column=4,padx=5,pady=5,sticky=W)

    #Dato
    lblDato=Label(window6,text="Dato:")
    lblDato.grid(row=1,column=3,padx=5,pady=5,sticky=E)
    entEmnekode=Entry(window6,width=10,state="readonly",textvariable=dato)
    entEmnekode.grid(row=1,column=4,padx=5,pady=5,sticky=W)

    #Romnr
    lblRomnr=Label(window6,text="Romnummer:")
    lblRomnr.grid(row=2,column=3,padx=5,pady=5,sticky=E)
    entRomnr=Entry(window6,width=4,textvariable=romnr)
    entRomnr.grid(row=2,column=4,padx=5,pady=5,sticky=W)

    #tekstboks
    txtboks=Text(window6,width=21,height=1)
    txtboks.grid(row=5,column=4,columnspan=2,padx=5,pady=5,sticky=W)

    #Knapper
    btnLagre=Button(window6,text="Lagre",command=lagreEndringer)
    btnLagre.grid(row=11,column=3,padx=5,pady=5,sticky=E)
    btnTilbake=Button(window6,text="Tilbake",command=window6.destroy)
    btnTilbake.grid(row=11,column=4,padx=5,pady=5,sticky=E)

#Sletting av eksisterende eksamen
def eksamensslettingWindow7():

    #Tømme søkefeltet for å gjøre klart for nytt søk
    def tomSokefelt():
        emnekode.set("")
        dato.set("")

    #Sletter eksamen fra database
    def slettEksamen():

        sletteEmnekode=emnekode.get()
        sletteDato=dato.get()
        
        slettemarkor=mindatabase.cursor()
        sletting=("DELETE FROM Eksamen WHERE Emnekode=%s and Dato=%s")
        slettedata=(sletteEmnekode,sletteDato)
        
        try:
            slettemarkor.execute(sletting,slettedata)
        except:
            txtboks.config(state=NORMAL)
            txtboks.delete("1.0","end")
            txtboks.insert("1.0","Eksamen kan ikke slettes")
            txtboks.config(state=DISABLED)
        else:
            mindatabase.commit()
            txtboks.config(state=NORMAL)
            txtboks.delete("1.0","end")
            txtboks.insert("1.0","Eksamen slettet")
            txtboks.config(state=DISABLED)

        slettemarkor.close()
        tomSokefelt()
    
    window7=Toplevel()
    window7.title("Eksamenssletting")

    #Variabel
    emnekode=StringVar()
    dato=StringVar()

    #Emnekode
    lblEmnekode=Label(window7,text="Legg inn emnekode:")
    lblEmnekode.grid(row=0,column=0,padx=5,pady=5,sticky=E)
    entEmnekode=Entry(window7,width=8,textvariable=emnekode)
    entEmnekode.grid(row=0,column=1,padx=5,pady=5,sticky=W)

    #Dato
    lblDato=Label(window7,text="Legg inn dato:")
    lblDato.grid(row=1,column=0,padx=5,pady=5,sticky=E)
    entDato=Entry(window7,width=8,textvariable=dato)
    entDato.grid(row=1,column=1,padx=5,pady=5,sticky=W)

    #Textbox
    txtboks=Text(window7,width=21,height=1)
    txtboks.grid(row=3,column=1,padx=5,pady=5,sticky=E)

    #Knapper
    btnSlette=Button(window7,text="Slett",command=slettEksamen)
    btnSlette.grid(row=11,column=3,padx=5,pady=5,sticky=E)
    btnTilbake=Button(window7,text="Tilbake",command=window7.destroy)
    btnTilbake.grid(row=11,column=4,padx=5,pady=5,sticky=E)

#Registrering av ny eksamensresultat
def resultatregistreringWindow8():

    #Henter studentnr på alle studenter som skal ha karakter i eksamen og lager innlesningsfelt dynamisk
    def HentstudentnrOgLagEntries():            

        #Henter informasjonen skrevet inn i innlesningsfeltene og lagrer dem i databasen
        def registrerResultater():

            eksamenEmne=emnekode.get()
            eksamenDato=dato.get()

            resultatmarkor=mindatabase.cursor()

            for i in range (0,len(listeStudentnr),1):
                resultat=entryListe[i][1].get()
                entryListe[i][1]=resultat

                sql=("UPDATE Eksamensresultat SET Karakter=%s WHERE Studentnr=%s AND Emnekode=%s AND Dato=%s AND Karakter IS NULL")
                data=(entryListe[i][1],entryListe[i][0],eksamenEmne,eksamenDato)

                resultatmarkor.execute(sql,data)

                mindatabase.commit()

            resultatmarkor.close()

        henteEmnekode=emnekode.get()
        henteDato=dato.get()

        hentemarkor=mindatabase.cursor()
        henteSql=("SELECT Studentnr FROM Eksamensresultat WHERE Emnekode=%s AND Dato=%s AND Karakter IS NULL")
        henteData=(henteEmnekode,henteDato)
        hentemarkor.execute(henteSql,henteData)

        listeStudentnr=[]
        for i in hentemarkor:
            listeStudentnr+=[i[0]]
        hentemarkor.close()
        
        entryListe=[]
        runde=0
        for i in range (0,len(listeStudentnr),1):
            studentnr=StringVar()
            lblStudentnr=Label(window8,text="Studentnr:")
            lblStudentnr.grid(row=i,column=0,padx=5,pady=5,sticky=E)
            entStudnr=Entry(window8,width=6,state="readonly",textvariable=studentnr)
            entStudnr.grid(row=i,column=1,padx=5,pady=5,sticky=W)
            lblResultat=Label(window8,text="Resultat")
            lblResultat.grid(row=i,column=2,padx=5,pady=5,sticky=E)
            entResultat=Entry(window8,width=2)
            entResultat.grid(row=i,column=3,padx=5,pady=5,sticky=W)

            entryListe+=[[listeStudentnr[i]]+[entResultat]]

            studentnr.set(listeStudentnr[runde])
            runde=runde+1
        
        btnLagre=Button(window8,text="Lagre",command=registrerResultater)
        btnLagre.grid(row=50,column=5,padx=5,pady=5,sticky=E)
    
    window8=Toplevel()
    window8.title("Registrering av eksamenresultater")

    #Variabler
    emnekode=StringVar()
    dato=StringVar()
    
    #Emnekode
    lblEmnekode=Label(window8,text="Legg inn emnekode:")
    lblEmnekode.grid(row=0,column=5,padx=5,pady=5,sticky=E)
    entEmnekode=Entry(window8,width=8,textvariable=emnekode)
    entEmnekode.grid(row=0,column=6,padx=5,pady=5,sticky=W)
    
    #Dato
    lblDato=Label(window8,text="Legg inn dato:")
    lblDato.grid(row=1,column=5,padx=5,pady=5,sticky=E)
    entDato=Entry(window8,width=8,textvariable=dato)
    entDato.grid(row=1,column=6,padx=5,pady=5,sticky=W)

    #Søkeknapp
    btnSok=Button(window8,text="Søk",command=HentstudentnrOgLagEntries)
    btnSok.grid(row=2,column=6,padx=5,pady=5,sticky=W)
    
    #knapper
    btnTilbake=Button(window8,text="Tilbake til hovedmeny",command=window8.destroy)
    btnTilbake.grid(row=50,column=6,padx=5,pady=5,sticky=E)

#Redigering av eksisterende eksamensresultat
def resultatredigeringWindow9():

    #Henter resultatinfo fra database basert på søk
    def hentResultatinfo():
        infStudentnr=studentnr.get()
        infEmnekode=emnekode.get()
        infDato=dato.get()

        hentemarkor=mindatabase.cursor()
        sqlHente=("SELECT Karakter FROM Eksamensresultat WHERE Studentnr=%s AND Emnekode=%s AND Dato=%s")
        dataHente=(infStudentnr,infEmnekode,infDato)

        hentemarkor.execute(sqlHente,dataHente)
        
        karakterliste=[]

        for i in hentemarkor:
            karakterliste+=i[0]

        karakter.set(karakterliste[0])
        hentemarkor.close()

    #Lagrer redigert informasjon til database
    def lagreInfo():

        lagreKarakter=karakter.get()
        lagerStudentnr=studentnr.get()
        lagreEmnekode=emnekode.get()
        lagreDato=dato.get()
        

        lagremarkor=mindatabase.cursor()

        sqlLagre=("UPDATE Eksamensresultat SET Karakter=%s WHERE Studentnr=%s AND Emnekode=%s AND Dato=%s AND Karakter IS NOT NULL")
        dataLagre=(lagreKarakter,lagerStudentnr,lagreEmnekode,lagreDato)
        try:
            lagremarkor.execute(sqlLagre,dataLagre)
        except:
            tekstboks.config(state=NORMAL)
            tekstboks.delete("1.0","end")
            tekstboks.insert("1.0","Resultat kan ikke endres")
            tekstboks.config(state=DISABLED)
        else:
            mindatabase.commit()
            tekstboks.config(state=NORMAL)
            tekstboks.delete("1.0","end")
            tekstboks.insert("1.0","Resultat endret")
            tekstboks.config(state=DISABLED)

        lagremarkor.close()
        tomEntryfelt()
        
    #Tømmer entryfelt for å gjøre klart for nytt søk
    def tomEntryfelt():
        studentnr.set("")
        emnekode.set("")
        dato.set("")
        karakter.set("")
    
    window9=Toplevel()
    window9.title("Redigere eksamensresultater")

    #Variabler
    studentnr=StringVar()
    emnekode=StringVar()
    dato=StringVar()
    karakter=StringVar()

    #Studentnr
    lblStudentnr=Label(window9,text="Legg inn studentnr:")
    lblStudentnr.grid(row=0,column=0,padx=5,pady=5,sticky=E)
    entStudentnr=Entry(window9,width=6,textvariable=studentnr)
    entStudentnr.grid(row=0,column=1,padx=5,pady=5,sticky=W)

    #Emnekode
    lblEmnekode=Label(window9,text="Legg inn emnekode:")
    lblEmnekode.grid(row=1,column=0,padx=5,pady=5,sticky=E)
    entEmnekode=Entry(window9,width=8,textvariable=emnekode)
    entEmnekode.grid(row=1,column=1,padx=5,pady=5,sticky=W)

    #Dato
    lblDato=Label(window9,text="Legg inn dato:")
    lblDato.grid(row=2,column=0,padx=5,pady=5,sticky=E)
    entDato=Entry(window9,width=8,textvariable=dato)
    entDato.grid(row=2,column=1,padx=5,pady=5,sticky=W)

    #Søkeknapp
    btnSok=Button(window9,text="Søk",command=hentResultatinfo)
    btnSok.grid(row=3,column=1,padx=5,pady=5,sticky=W)

    #Karakter
    lblKarakter=Label(window9,text="Karakter")
    lblKarakter.grid(row=4,column=0,padx=5,pady=5,sticky=E)
    entKarakter=Entry(window9,width=2,textvariable=karakter)
    entKarakter.grid(row=4,column=1,padx=5,pady=5,sticky=W)

    #Tekstboks
    tekstboks=Text(window9,width=15,height=1)
    tekstboks.grid(row=5,column=1,padx=5,pady=5,sticky=W)

    #Knapper
    btnLagre=Button(window9,text="Lagre",command=lagreInfo)
    btnLagre.grid(row=6,column=3,padx=5,pady=5,sticky=E)
    btnTilbake=Button(window9,text="Tilbake til hovedmeny",command=window9.destroy)
    btnTilbake.grid(row=6,column=4,padx=5,pady=5,sticky=E)

#Sletting av eksisterende eksamensresultat uten karakter
def resultatslettingWindow10():
    
    #Kontrollere informasjon med database
    def hentInfo():

        henteStudnr=studentnr.get()
        henteEmnekode=emnekode.get()
        henteDato=dato.get()

        hentemarkor=mindatabase.cursor()
        henteSql=("SELECT * FROM Eksamensresultat WHERE Studentnr=%s AND Emnekode=%s and Dato=%s AND Karakter IS NULL")
        henteData=(henteStudnr,henteEmnekode,henteDato)
        hentemarkor.execute(henteSql,henteData)

        sletteliste=[]

        for i in hentemarkor:
            sletteliste+=[i]

        hentemarkor.close()

        if sletteliste==[]:
            tekstboks.config(state=NORMAL)
            tekstboks.delete("1.0","end")
            tekstboks.insert("1.0","Student har resultat og kan ikke slettes")
            tekstboks.config(state=DISABLED)
            btnSlette["state"]=DISABLED
        else:
            tekstboks.config(state=NORMAL)
            tekstboks.delete("1.0","end")
            tekstboks.insert("1.0","Student har ikke resultat og kan slettes")
            tekstboks.config(state=DISABLED)
            btnSlette["state"]=NORMAL

    #Slette informasjon fra database
    def sletteksamensresultat():
        
        sletteStudnr=studentnr.get()
        sletteEmnekode=emnekode.get()
        sletteDato=dato.get()

        slettemarkor=mindatabase.cursor()
        sletteSql=("DELETE FROM Eksamensresultat WHERE Studentnr=%s AND Emnekode=%s AND Dato=%s AND Karakter IS NULL")
        slettesData=(sletteStudnr,sletteEmnekode,sletteDato)
        slettemarkor.execute(sletteSql,slettesData)
        mindatabase.commit()
        slettemarkor.close()
        tomEntryfelt()
    
    #Tømme entryfelt for å gjøre klart til nytt søk
    def tomEntryfelt():
        studentnr.set("")
        emnekode.set("")
        dato.set("")

    window10=Toplevel()
    window10.title("Slette eksamensresultat")

    #Variabler
    studentnr=StringVar()
    emnekode=StringVar()
    dato=StringVar()
    sletteinfo=StringVar()

    #Studentnr
    lblStudentnr=Label(window10,text="Legg inn studentnr:")
    lblStudentnr.grid(row=0,column=0,padx=5,pady=5,sticky=E)
    entStudentnr=Entry(window10,width=6,textvariable=studentnr)
    entStudentnr.grid(row=0,column=1,padx=5,pady=5,sticky=W)

    #Emnekode
    lblEmnekode=Label(window10,text="Legg inn emnekode")
    lblEmnekode.grid(row=1,column=0,padx=5,pady=5,sticky=E)
    entEmnekode=Entry(window10,width=8,textvariable=emnekode)
    entEmnekode.grid(row=1,column=1,padx=5,pady=5,sticky=W)

    #Dato
    lblDato=Label(window10,text="Legg inn dato:")
    lblDato.grid(row=2,column=0,padx=5,pady=5,sticky=E)
    entDato=Entry(window10,width=8,textvariable=dato)
    entDato.grid(row=2,column=1,padx=5,pady=5,sticky=W)

    #Søkeknapp
    btnSok=Button(window10,text="Søk",command=hentInfo)
    btnSok.grid(row=3,column=1,padx=5,pady=5,sticky=W)

    #Tekstboks
    tekstboks=Text(window10,width=40,height=1)
    tekstboks.grid(row=4,column=1,padx=5,pady=5,sticky=W)

    #Knapper
    btnSlette=Button(window10,text="Slett eksamensregistrering",command=sletteksamensresultat)
    btnSlette.grid(row=12,column=5,padx=5,pady=5,sticky=E)
    btnTilbake=Button(window10,text="Tilbake til hovedmeny",command=window10.destroy)
    btnTilbake.grid(row=12,column=6,padx=5,pady=5,sticky=E)

#Utskrift av alle eksamener på en dato
def eksammensutksiftDatoWindow11():

    #Hente ut informasjon fra database og presentere det i tekstboks
    def hentInfo():
        sokDato=dato.get()

        hentemarkor=mindatabase.cursor()

        henteSql=("SELECT * FROM Eksamen WHERE Dato=%s")
        henteData=(sokDato,)
        hentemarkor.execute(henteSql,henteData)

        henteListe=[]
        for i in hentemarkor:
            henteListe+=[[i[0],i[1],i[2]]]

        tekstboks.config(state=NORMAL)
        tekstboks.delete("1.0","end")

        for n in range(len(henteListe)):
            tekstboks.insert("end",henteListe[n][0]+" "+str(henteListe[n][1])+" "+henteListe[n][2]+"\n")
        
        tekstboks.config(state=DISABLED)
        hentemarkor.close()

    window11=Toplevel()
    window11.title("Eksamenssøk Dato")

    #Variabler
    dato=StringVar()

    #Dato
    lblDato=Label(window11,text="Legg inn dato:")
    lblDato.grid(row=0,column=0,padx=5,pady=5,sticky=E)
    entDato=Entry(window11,width=8,textvariable=dato)
    entDato.grid(row=0,column=1,padx=5,pady=5,sticky=W)

    #Søkeknapp
    btnSok=Button(window11,text="Søk",command=hentInfo)
    btnSok.grid(row=1,column=1,padx=5,pady=5,sticky=W)

    #tekstboks
    tekstboks=Text(window11,width=24,height=10)
    tekstboks.grid(row=2,column=1,padx=5,pady=5)

    #Knapper
    btnTilbake=Button(window11,text="Tilbake til hovedmeny",command=window11.destroy)
    btnTilbake.grid(row=3,column=2,padx=5,pady=5,sticky=E)

#Utskrift av alle eksamener i en periode
def eksamensutskriftPeriodeWindow12():

    #Henter ut alle eksamen i en periode og presenterer dem i en tekstboks
    def hentInfo():
        sokDatoFra=datoFra.get()
        sokDatoTil=datoTil.get()

        hentemarkor=mindatabase.cursor()

        henteSql=("SELECT * FROM Eksamen WHERE Dato BETWEEN %s AND %s")
        henteData=(sokDatoFra,sokDatoTil)
        hentemarkor.execute(henteSql,henteData)


        henteListe=[]
        for i in hentemarkor:
            henteListe+=[[i[0],i[1],i[2]]]


        tekstboks.config(state=NORMAL)
        tekstboks.delete("1.0","end")

        for n in range(len(henteListe)):
            tekstboks.insert("end",henteListe[n][0]+" "+str(henteListe[n][1])+" "+henteListe[n][2]+"\n")
        
        tekstboks.config(state=DISABLED)
        hentemarkor.close()


    window12=Toplevel()
    window12.title("Eksamenssøk Periode")

    #Variabler
    datoFra=StringVar()
    datoTil=StringVar()

    #Dato Fra
    lblDatoFra=Label(window12,text="Legg inn dato fra:")
    lblDatoFra.grid(row=0,column=0,padx=5,pady=5,sticky=E)
    lblDatoFra=Entry(window12,width=8,textvariable=datoFra)
    lblDatoFra.grid(row=0,column=1,padx=5,pady=5,sticky=W)

    #Dato Til
    lblDatoTil=Label(window12,text="Legg inn dato til:")
    lblDatoTil.grid(row=0,column=2,padx=5,pady=5,sticky=E)
    lblDatoTil=Entry(window12,width=8,textvariable=datoTil)
    lblDatoTil.grid(row=0,column=3,padx=5,pady=5,sticky=W)

    #Søkeknapp
    btnSok=Button(window12,text="Søk",command=hentInfo)
    btnSok.grid(row=1,column=1,padx=5,pady=5,sticky=W)

    #tekstboks
    tekstboks=Text(window12,width=24,height=10)
    tekstboks.grid(row=2,column=1,padx=5,pady=5)

    #Knapper
    btnTilbake=Button(window12,text="Tilbake til hovedmeny",command=window12.destroy)
    btnTilbake.grid(row=3,column=4,padx=5,pady=5,sticky=E)

#Utskrift av alle eksamenresultater på et emne
def eksamensresultaterEmneWindow13():

    #Hente informasjon fra database og presentere det i tekstboksen
    def hentInfo():
        henteEmnekode=emnekode.get()
        henteDato=dato.get()

        hentemarkor=mindatabase.cursor()

        henteSql=("SELECT * FROM Eksamensresultat WHERE Emnekode=%s AND Dato=%s ORDER BY Studentnr")
        henteData=(henteEmnekode,henteDato)
        hentemarkor.execute(henteSql,henteData)

        resultatliste=[]
        for i in hentemarkor:
            resultatliste+=[[i[0],i[1],str(i[2]),i[3]]]

        hentemarkor.close()

        txtEksamensresultater.config(state=NORMAL)
        txtEksamensresultater.delete("1.0","end")
        for n in range (len(resultatliste)):
            txtEksamensresultater.insert("end",resultatliste[n][0]+" "+resultatliste[n][1]+" "+resultatliste[n][2]+" "+resultatliste[n][3]+"\n")
        txtEksamensresultater.config(state=DISABLED)


    window13=Toplevel()
    window13.title("Eksamensresultater for et emne")

    #Variabler
    emnekode=StringVar()
    dato=StringVar()

    #Emnekode
    lblEmnekode=Label(window13,text="Legg inn emnekode")
    lblEmnekode.grid(row=0,column=0,padx=5,pady=5,sticky=E)
    entEmnekode=Entry(window13,width=8,textvariable=emnekode)
    entEmnekode.grid(row=0,column=1,padx=5,pady=5,sticky=W)

    #Dato
    lblDato=Label(window13,text="Legg inn dato")
    lblDato.grid(row=0,column=2,padx=5,pady=5,sticky=E)
    entDato=Entry(window13,width=8,textvariable=dato)
    entDato.grid(row=0,column=3,padx=5,pady=5,sticky=W)

    #Søkeknapp
    btnSok=Button(window13,text="Søk",command=hentInfo)
    btnSok.grid(row=1,column=1,padx=5,pady=5,sticky=W)

    #Tekstboks
    txtEksamensresultater=Text(window13,width=30,height=10)
    txtEksamensresultater.grid(row=2,column=1,padx=5,pady=5,sticky=W)

    #Knapper
    btnTilbake=Button(window13,text="Tilbake til hovedmeny",command=window13.destroy)
    btnTilbake.grid(row=3,column=3,padx=5,pady=5,sticky=E)

#Utskrift av karakterstatestikk for en eksamen
def karakterstatestikkWindow14():

    #Henter ut statestikk fra database og presenterer det i tekstboks
    def henteStatestikk():
        henteEmnekode=emnekode.get()
        henteDato=dato.get()

        hentemarkor=mindatabase.cursor()
        henteSql=("SELECT eksamensresultat.emnekode, emne.emnenavn, emne.Studiepoeng, eksamensresultat.karakter, COUNT(eksamensresultat.studentnr) AS Antall FROM emne JOIN eksamensresultat ON eksamensresultat.emnekode=emne.emnekode WHERE eksamensresultat.emnekode=%s AND eksamensresultat.dato=%s AND karakter IS NOT NULL GROUP BY eksamensresultat.emnekode, emne.emnenavn, emne.Studiepoeng, eksamensresultat.karakter ORDER BY eksamensresultat.karakter")
        henteData=(henteEmnekode,henteDato)
        hentemarkor.execute(henteSql,henteData)

        statestikkliste=[]
        for n in hentemarkor:
            statestikkliste+=[[n[0],n[1],str(n[2]),n[3],str(n[4])]]

        hentemarkor.close()
        
        txtEksamenstatestikk.config(state=NORMAL)
        txtEksamenstatestikk.delete("1.0","end")
        for i in range(len(statestikkliste)):
            txtEksamenstatestikk.insert("end",statestikkliste[i][0]+" "+statestikkliste[i][1]+" "+statestikkliste[i][2]+" "+statestikkliste[i][3]+" "+"Antall:"+" "+statestikkliste[i][4]+"\n")
        txtEksamenstatestikk.config(state=DISABLED)

    window14=Toplevel()
    window14.title("Karakterstatestikk for en eksamen")

    #Variabler
    emnekode=StringVar()
    dato=StringVar()

    #Emnekode
    lblEmnekode=Label(window14,text="Legg inn emnekode")
    lblEmnekode.grid(row=0,column=0,padx=5,pady=5,sticky=E)
    entEmnekode=Entry(window14,width=8,textvariable=emnekode)
    entEmnekode.grid(row=0,column=1,padx=5,pady=5,sticky=W)

    #Dato
    lblDato=Label(window14,text="Legg inn dato")
    lblDato.grid(row=0,column=2,padx=5,pady=5,sticky=E)
    entDato=Entry(window14,width=8,textvariable=dato)
    entDato.grid(row=0,column=3,padx=5,pady=5,sticky=W)

    #Søkeknapp
    btnSok=Button(window14,text="Søk",command=henteStatestikk)
    btnSok.grid(row=1,column=1,padx=5,pady=5,sticky=W)

    #Tekstboks
    txtEksamenstatestikk=Text(window14,width=55,height=10)
    txtEksamenstatestikk.grid(row=2,column=1,padx=5,pady=5,sticky=W)

    #Knapper
    btnTilbake=Button(window14,text="Tilbake til hovedmeny",command=window14.destroy)
    btnTilbake.grid(row=3,column=2,padx=5,pady=5,sticky=E)

#Utskrift av eksamensresultater for en student
def eksamensresultaterStudentWindow15():

    #Henter resultater for student og presenterer i tekstboks
    def henteResultater():

        henteStudentnr=studentnr.get()

        hentemarkor=mindatabase.cursor()
        henteSql=("SELECT eksamensresultat.emnekode, emne.emnenavn, emne.Studiepoeng, eksamensresultat.dato, eksamensresultat.karakter FROM emne JOIN eksamensresultat ON eksamensresultat.emnekode=emne.emnekode WHERE eksamensresultat.studentnr=%s AND karakter IS NOT NULL GROUP BY eksamensresultat.emnekode, emne.emnenavn, emne.Studiepoeng, eksamensresultat.dato, eksamensresultat.karakter ORDER BY eksamensresultat.dato;")
        henteData=(henteStudentnr,)
        hentemarkor.execute(henteSql,henteData)

        studentresultatliste=[]
        for n in hentemarkor:
            studentresultatliste+=[[n[0],n[1],str(n[2]),str(n[3]),n[4]]]

        hentemarkor.close()

        txtStudentEksamensresultater.config(state=NORMAL)
        txtStudentEksamensresultater.delete("1.0","end")
        for i in range(len(studentresultatliste)):
            txtStudentEksamensresultater.insert("end",studentresultatliste[i][0]+" "+studentresultatliste[i][1]+" "+studentresultatliste[i][2]+" "+studentresultatliste[i][3]+", Karakter: "+studentresultatliste[i][4]+"\n")
        txtStudentEksamensresultater.config(state=DISABLED)

    window15=Toplevel()
    window15.title("Eksamensresultater for en student")

    #Variabler
    studentnr=StringVar()

    #Studentnr
    lblStudentnr=Label(window15,text="Legg inn studentnr:")
    lblStudentnr.grid(row=0,column=0,padx=5,pady=5,sticky=E)
    entStudentnr=Entry(window15,width=8,textvariable=studentnr)
    entStudentnr.grid(row=0,column=1,padx=5,pady=5,sticky=W)

    #Søkeknapp
    btnSok=Button(window15,text="Søk",command=henteResultater)
    btnSok.grid(row=1,column=1,padx=5,pady=5,sticky=W)

    #Tekstboks
    txtStudentEksamensresultater=Text(window15,width=70,height=10)
    txtStudentEksamensresultater.grid(row=2,column=1,padx=5,pady=5,sticky=W)

    #Knapper
    btnTilbake=Button(window15,text="Tilbake til hovedmeny",command=window15.destroy)
    btnTilbake.grid(row=3,column=2,padx=5,pady=5,sticky=E)

#Utskrift av vitnemål for en student
def vitnemålWindow16():

    #Henter vitnemål fra database og presenterer i tekstboks
    def hentVitnemål():
        henteStudentnr=studentnr.get()

        vitnemalmarkor=mindatabase.cursor()
        vitnemalSql=("SELECT eksamensresultat.emnekode, emne.emnenavn, eksamensresultat.dato, MIN(eksamensresultat.karakter) AS HoyestKarakter, emne.Studiepoeng FROM eksamensresultat JOIN Emne ON eksamensresultat.emnekode=emne.emnekode WHERE Studentnr=%s AND karakter IS NOT NULL AND Karakter!='F' GROUP BY eksamensresultat.emnekode, emne.emnenavn")
        vitnemalData=(henteStudentnr,)
        vitnemalmarkor.execute(vitnemalSql,vitnemalData)

        vitnemalliste=[]
        for i in vitnemalmarkor:
            vitnemalliste+=[[i[0],i[1],str(i[2]),i[3],i[4]]]
            
        vitnemalmarkor.close()

        txtVitnemal.config(state=NORMAL)
        txtVitnemal.delete("1.0","end")
        for i in range(len(vitnemalliste)):
            txtVitnemal.insert("end",vitnemalliste[i][0]+", "+vitnemalliste[i][1]+", "+vitnemalliste[i][2]+", Karakter: "+vitnemalliste[i][3]+"\n")
        txtVitnemal.config(state=DISABLED)

        studpoeng=0
        for n in range (len(vitnemalliste)):
            studpoeng+=vitnemalliste[n][4]

        studiepoeng.set(str(studpoeng))

    window16=Toplevel()
    window16.title("Vitnemålutskrift")

    #Variabler
    studentnr=StringVar()
    studiepoeng=StringVar()

    #Studentnr
    lblStudentnr=Label(window16,text="Legg inn studentnr:")
    lblStudentnr.grid(row=0,column=0,padx=5,pady=5,sticky=E)
    entStudentnr=Entry(window16,width=8,textvariable=studentnr)
    entStudentnr.grid(row=0,column=1,padx=5,pady=5,sticky=W)

    #Søkeknapp
    btnSok=Button(window16,text="Søk",command=hentVitnemål)
    btnSok.grid(row=1,column=1,padx=5,pady=5,sticky=W)

    #Tekstboks
    txtVitnemal=Text(window16,width=70,height=10)
    txtVitnemal.grid(row=2,column=1,padx=5,pady=5,sticky=W)

    #Studiepoeng
    lblStudiepoeng=Label(window16,text="Studiepoeng for student")
    lblStudiepoeng.grid(row=3,column=0,padx=5,pady=5,sticky=E)
    entStudiepoeng=Entry(window16,width=4,state="readonly",textvariable=studiepoeng)
    entStudiepoeng.grid(row=3,column=1,padx=5,pady=5,sticky=W) 

    #Knapper
    btnTilbake=Button(window16,text="Tilbake til hovedmeny",command=window16.destroy)
    btnTilbake.grid(row=4,column=2,padx=5,pady=5,sticky=E)

#Eksamensoppmelding av studenter
def eksamensoppmeldingWindow17():

    #Lagrere oppmelding til database og gir tilbakemelding til bruker i tekstboks
    def lagreOppmelding():
        oppEmnekode=emnekode.get()
        oppDato=dato.get()
        oppStudentnr=studentnr.get()

        oppmeldingsmarkor=mindatabase.cursor()
        oppmeldingSql=("INSERT INTO Eksamensresultat (Studentnr, Emnekode, Dato, Karakter) VALUES (%s,%s,%s,NULL)")
        oppmeldingData=(oppStudentnr,oppEmnekode,oppDato)

        try:
            oppmeldingsmarkor.execute(oppmeldingSql,oppmeldingData)
        except:
            txtTilbakemelding.config(state=NORMAL)
            txtTilbakemelding.delete("1.0","end")
            txtTilbakemelding.insert("end","Student kan ikke meldes opp til eksamen")
            txtTilbakemelding.config(state=DISABLED)
        else:
            txtTilbakemelding.config(state=NORMAL)
            txtTilbakemelding.delete("1.0","end")
            txtTilbakemelding.insert("end","Student registrert")
            txtTilbakemelding.config(state=DISABLED)
            mindatabase.commit()
            studentnr.set("")
        oppmeldingsmarkor.close()

    window17=Toplevel()
    window17.title("Eksamensoppmelding")

    #Variabler
    emnekode=StringVar()
    dato=StringVar()
    studentnr=StringVar()

    #emnekode
    lblEmnekode=Label(window17,text="Legg inn emnekode:")
    lblEmnekode.grid(row=0,column=0,padx=5,pady=5,sticky=E)
    entEmnekode=Entry(window17,width=8,textvariable=emnekode)
    entEmnekode.grid(row=0,column=1,padx=5,pady=5,sticky=W)

    #Dato
    lblDato=Label(window17,text="Legg inn dato:")
    lblDato.grid(row=1,column=0,padx=5,pady=5,sticky=E)
    entDato=Entry(window17,width=8,textvariable=dato)
    entDato.grid(row=1,column=1,padx=5,pady=5,sticky=W)

    #Studentnr
    lblStudentnr=Label(window17,text="Legg inn studentnr")
    lblStudentnr.grid(row=2,column=0,padx=5,pady=5,sticky=E)
    entStudentnr=Entry(window17,width=6,textvariable=studentnr)
    entStudentnr.grid(row=2,column=1,padx=5,pady=5,sticky=W)

    #Tekstboks
    txtTilbakemelding=Text(window17,width=40,height=1)
    txtTilbakemelding.grid(row=3,column=1,padx=5,pady=5)
    txtTilbakemelding.config(state=DISABLED)

    #Knapper
    btnLagre=Button(window17,text="Lagre",command=lagreOppmelding)
    btnLagre.grid(row=4,column=1,padx=5,pady=5,sticky=E)
    btnTilbake=Button(window17,text="Tilbake til hovedmeny",command=window17.destroy)
    btnTilbake.grid(row=4,column=2,padx=5,pady=5,sticky=E)

#Hovedvindu
window=Tk()
window.title("Eksamenshåndtering")

#Label og knapper for studenthåndtering
lblStudenthåndtering=Label(window,text="Studenthåndtering")
lblStudenthåndtering.grid(row=0,columnspan=3,padx=5,pady=5,sticky=S)
btnStudentoppretting=Button(window,text="Registrerer ny student",command=studentregistreringWindow2)
btnStudentoppretting.grid(row=1,column=0,padx=5,pady=5,sticky=NE)
btnStudentendring=Button(window,text="Rediger eksisterende student",command=studentredigeringWindow3)
btnStudentendring.grid(row=1,column=1,padx=5,pady=5,sticky=N)
btnStudentsletting=Button(window,text="Slett eksisterende student",command=studentslettingWindow4)
btnStudentsletting.grid(row=1,column=2,padx=5,pady=5,sticky=NW)

#Label og knapper for eksamenshåndtering
lblEksamenshåndtering=Label(window,text="Eksamenshåndtering")
lblEksamenshåndtering.grid(row=2,columnspan=3,padx=5,pady=5,sticky=S)
btnEksamensregistrering=Button(window,text="Registerer ny eksamen",command=eksamensregistreringWindow5)
btnEksamensregistrering.grid(row=3,column=0,padx=5,pady=5,sticky=NE)
btnEksamensredigering=Button(window,text="Rediger eksisterende eksamen",command=eksamensredigeringWindow6)
btnEksamensredigering.grid(row=3,column=1,padx=5,pady=5,sticky=N)
btnEksamenssletting=Button(window,text="Slett eksisterende eksamen",command=eksamensslettingWindow7)
btnEksamenssletting.grid(row=3,column=2,padx=5,pady=5,sticky=NW)

#Label og knapper for eksamensresultathåndtering
lblResultathåndtering=Label(window,text="Håndtering av Eksamensresultater")
lblResultathåndtering.grid(row=4,columnspan=4,padx=5,pady=5,sticky=S)
btnResultatregistrering=Button(window,text="Registrer nye eksamensresultater",command=resultatregistreringWindow8)
btnResultatregistrering.grid(row=5,column=0,padx=5,pady=5,sticky=NE)
btnResultatredigering=Button(window,text="Rediger eksisterende eksamensresultat",command=resultatredigeringWindow9)
btnResultatredigering.grid(row=5,column=1,padx=5,pady=5,sticky=N)
btnResultatsletting=Button(window,text="Slett eksisterende eksamensresultat",command=resultatslettingWindow10)
btnResultatsletting.grid(row=5,column=2,padx=5,pady=5,sticky=NW)
btnEksamensoppmelding=Button(window,text="Meld opp studenter til eksamen",command=eksamensoppmeldingWindow17)
btnEksamensoppmelding.grid(row=7,column=0,padx=5,pady=5,sticky=NE)

#Label og knapper for diverse utskrifter
lblDivUtskrifter=Label(window,text="Diverse Utskrifter")
lblDivUtskrifter.grid(row=8,columnspan=3,padx=5,pady=5)
btnEksamenDato=Button(window,text="Eksamenssøk spesifik dato",command=eksammensutksiftDatoWindow11)
btnEksamenDato.grid(row=9,column=0,padx=5,pady=5,sticky=NE)
btnEksamenPeriode=Button(window,text="Eksamenssøk periode",command=eksamensutskriftPeriodeWindow12)
btnEksamenPeriode.grid(row=9,column=1,padx=5,pady=5,sticky=N)
btnResultaterEmne=Button(window,text="Eksamensresultater emne",command=eksamensresultaterEmneWindow13)
btnResultaterEmne.grid(row=9,column=2,padx=5,pady=5,sticky=NW)
btnResultaterStatestikk=Button(window,text="Karakterstatestikk",command=karakterstatestikkWindow14)
btnResultaterStatestikk.grid(row=10,column=0,padx=5,pady=5,sticky=NE)
btnStudentresultater=Button(window,text="Student eksamensresultater",command=eksamensresultaterStudentWindow15)
btnStudentresultater.grid(row=10,column=1,padx=5,pady=5,sticky=N)
btnVitnemal=Button(window,text="Vitnemålutskrift",command=vitnemålWindow16)
btnVitnemal.grid(row=10,column=2,padx=5,pady=5,sticky=NW)

#Avsluttningsknapp
btnAvslutt=Button(window,text="Avslutt",command=window.destroy)
btnAvslutt.grid(row=11,column=5,padx=5,pady=5, sticky=E)

window.mainloop()
mindatabase.close()
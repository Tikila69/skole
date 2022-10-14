import mysql.connector
from tkinter import *

mindatabase=mysql.connector.connect(host="localhost",port="3306",user="root", password="Icastfireball20",db="heltnydatabase")


def window2():

    def henteInfoW2(event):
        valg=listeVarer.get(listeVarer.curselection())

        lagermarkor=mindatabase.cursor()
        lagermarkor.execute("SELECT Betegnelse, Pris, Antall FROM Vare")

        for i in lagermarkor:
            if valg==i[0]:
                pris.set(i[1])
                antall.set(i[2])
        lagermarkor.close()


    window2=Toplevel()
    window2.title=("Se Varebeholdning")
    

    Yscroll=Scrollbar(window2,orient=VERTICAL)
    Yscroll.grid(row=0,column=2,rowspan=10,padx=(0,100),pady=5,sticky=NS)

    innholdListeVarer=StringVar()
    listeVarer=Listbox(window2,width=50,height=10,listvariable=innholdListeVarer,yscrollcommand=Yscroll.set)
    listeVarer.grid(row=0,column=1,rowspan=10,padx=(100,0),pady=5,sticky=E)
    innholdListeVarer.set(tuple(liste))
    Yscroll["command"]=listeVarer.yview

    lblPris=Label(window2,text="Pris:")
    lblPris.grid(row=0,column=3,padx=5,pady=5,sticky=E)

    lblAntall=Label(window2,text="Antall:")
    lblAntall.grid(row=1,column=3,padx=5,pady=5,sticky=E)
    
    pris=StringVar()
    entPris=Entry(window2,width=6,state="readonly",textvariable=pris)
    entPris.grid(row=0,column=4,padx=5,pady=5,sticky=W)

    antall=StringVar()
    entAntall=Entry(window2,width=6,state="readonly",textvariable=antall)
    entAntall.grid(row=1,column=4,padx=5,pady=5,sticky=W)

    listeVarer.bind("<<ListboxSelect>>",henteInfoW2)

    btnTilbake=Button(window2,text="Tilbake til hovedmeny",command=window2.destroy)
    btnTilbake.grid(row=11,column=4,padx=5,pady=5,sticky=SW)

def window3():

    def lagreNyeVarer():

        varenr=vnr.get()
        varenavn=vnavn.get()
        pris=vpris.get()
        katnr=vkatNr.get()
        antall=vantall.get()
        hylle=vhylle.get()

        settinnMarkor=mindatabase.cursor()

        settinnvare=("INSERT INTO Vare"
                    "(Vnr,Betegnelse,Pris,KatNr,Antall,Hylle)"
                    "VALUES(%s,%s,%s,%s,%s,%s)")
        nyData=(varenr,varenavn,pris,katnr,antall,hylle)

        settinnMarkor.execute(settinnvare,nyData)
        mindatabase.commit()

    window3=Toplevel()
    window3.title("Vareregistrering")

    #Labels
    lblVarenr=Label(window3,text="Varenr:")
    lblVarenr.grid(row=0,column=0,padx=5,pady=5,sticky=E)

    lblVarenavn=Label(window3,text="Varenavn:")
    lblVarenavn.grid(row=1,column=0,padx=5,pady=5,sticky=E)

    lblPris=Label(window3,text="Pris:")
    lblPris.grid(row=2,column=0,padx=5,pady=5,sticky=E)

    lblKatnr=Label(window3,text="Kategori nr:")
    lblKatnr.grid(row=3,column=0,padx=5,pady=5,sticky=E)

    lblAntall=Label(window3,text="Antall:")
    lblAntall.grid(row=4,column=0,padx=5,pady=5,sticky=E)

    lblHylle=Label(window3,text="Hylle:")
    lblHylle.grid(row=5,column=0,padx=5,pady=5,sticky=E)

    #Innlesningsfelt
    vnr=StringVar()
    entVarenr=Entry(window3,width=6,textvariable=vnr)
    entVarenr.grid(row=0,column=1,padx=5,pady=5,sticky=W)

    vnavn=StringVar()
    entVarenavn=Entry(window3,width=20,textvariable=vnavn)
    entVarenavn.grid(row=1,column=1,padx=5,pady=5,sticky=W)

    vpris=StringVar()
    entPris=Entry(window3,width=6,textvariable=vpris)
    entPris.grid(row=2,column=1,padx=5,pady=5,sticky=W)

    vkatNr=StringVar()
    entKatnr=Entry(window3,width=2,textvariable=vkatNr)
    entKatnr.grid(row=3,column=1,padx=5,pady=5,sticky=W)

    vantall=StringVar()
    entAntall=Entry(window3,width=4,textvariable=vantall)
    entAntall.grid(row=4,column=1,padx=5,pady=5,sticky=W)

    vhylle=StringVar()
    entHylle=Entry(window3,width=3,textvariable=vhylle)
    entHylle.grid(row=5,column=1,padx=5,pady=5,sticky=W)

    #Knapper
    btnLagre=Button(window3,text="Lagre", command=lagreNyeVarer)
    btnLagre.grid(row=11,column=2,padx=5,pady=5,sticky=E)

    btnTilbake=Button(window3,text="Tilbake til hovedmeny",command=window3.destroy)
    btnTilbake.grid(row=11,column=3,padx=5,pady=5,sticky=E)

def window4():

    def lagreNyBeholdning():

        endringMarkor=mindatabase.cursor()
        
        endreVare=("UPDATE Vare SET Antall= %s WHERE Betegnelse=%s")
        endreData=(nyLagerbeholdning.get(),varenavn.get())

        endringMarkor.execute(endreVare, endreData)
        mindatabase.commit()
        endringMarkor.close()

    def hentBeholdning(event):
        valg=listVarer.get(listVarer.curselection())

        lagermarkor=mindatabase.cursor()
        lagermarkor.execute("SELECT Betegnelse, Antall FROM Vare")

        for row in lagermarkor:
            if valg==row[0]:
                lagerholdning.set(row[1])
                varenavn.set(row[0])
        lagermarkor.close()


    window4=Toplevel()
    window4.title=("Endre Varebeholdning")

    yScroll=Scrollbar(window4,orient=VERTICAL)
    yScroll.grid(row=0,column=2,rowspan=10,padx=(0,100),pady=5,sticky=NS)

    innholdListeVarer=StringVar()
    listVarer=Listbox(window4,width=50,height=10,listvariable=innholdListeVarer,yscrollcommand=yScroll.set)
    listVarer.grid(row=0,column=1,rowspan=10,padx=(100,0),pady=5,sticky=E)
    innholdListeVarer.set(tuple(liste))
    yScroll["command"]=listVarer.yview

    lblVarebeholdning=Label(window4,text="Nåværende varebeholdning")
    lblVarebeholdning.grid(row=0,column=3,padx=5,pady=5,sticky=E)

    lblVarebeholdningNy=Label(window4,text="Ny varebeholdning")
    lblVarebeholdningNy.grid(row=1,column=3,padx=5,pady=5,sticky=E)

    varenavn=StringVar()
    lagerholdning=StringVar()
    entBeholdning=Entry(window4,width=10,state="readonly", textvariable=lagerholdning)
    entBeholdning.grid(row=0,column=4,padx=5,pady=5,sticky=E)

    nyLagerbeholdning=StringVar()
    entNyBeholdning=Entry(window4,width=10,textvariable=nyLagerbeholdning)
    entNyBeholdning.grid(row=1,column=4,padx=5,pady=5,sticky=E)

    listVarer.bind("<<ListboxSelect>>",hentBeholdning)

    btnLagre=Button(window4,text="Lagre",command=lagreNyBeholdning)
    btnLagre.grid(row=11,column=3,padx=5,pady=5,sticky=E)

    btnTilbake=Button(window4,text="Tilbake til hovedmeny",command=window4.destroy)
    btnTilbake.grid(row=11,column=4,padx=5,pady=5,sticky=E)

def window5():

    def SletteVare():
        sletteMarkor=mindatabase.cursor()

        slettVare=("DELETE FROM Vare WHERE Betegnelse=%s")
        slettData=(betegnelse.get(),)
        
        sletteMarkor.execute(slettVare, slettData)
        mindatabase.commit()
        sletteMarkor.close()

    def henteVare(event):
        valg=listeVarer.get(listeVarer.curselection())

        lagermarkor=mindatabase.cursor()
        lagermarkor.execute("SELECT VNr, Betegnelse FROM Vare")

        for i in lagermarkor:
            if valg==i[1]:
                betegnelse.set(i[1])
        lagermarkor.close()
    

    window5=Toplevel()
    window5.title=("Varesletting")
    
    Yscroll=Scrollbar(window5,orient=VERTICAL)
    Yscroll.grid(row=0,column=2,rowspan=10,padx=(0,100),pady=5,sticky=NS)

    betegnelse=StringVar()
    innholdListeVarer=StringVar()

    listeVarer=Listbox(window5,width=50,height=10,listvariable=innholdListeVarer,yscrollcommand=Yscroll.set)
    listeVarer.grid(row=0,column=1,rowspan=10,padx=(100,0),pady=5,sticky=E)
    innholdListeVarer.set(tuple(liste))
    Yscroll["command"]=listeVarer.yview

    listeVarer.bind("<<ListboxSelect>>", henteVare)

    btnSlette=Button(window5,text="Slett Vare",command=SletteVare)
    btnSlette.grid(row=11,column=2,padx=5,pady=5,sticky=E)

    btnTilbake=Button(window5,text="Tilbake til hovedmeny",command=window5.destroy)
    btnTilbake.grid(row=11,column=3,padx=5,pady=5,sticky=E)

window=Tk()
window.title("My masterpiese")

varemarkor=mindatabase.cursor()
varemarkor.execute("SELECT * FROM vare")

liste=[]

for row in varemarkor:
    liste+=[row[1]]
    

btnWindow2=Button(window,text="Se Varebeholdning",command=window2)
btnWindow2.grid(row=0,column=0,padx=5,pady=5,sticky=W)

btnWindow3=Button(window,text="Vareregistrering",command=window3)
btnWindow3.grid(row=0,column=1,padx=5,pady=5,sticky=W)

btnWindow4=Button(window,text="Endre Varebeholdning",command=window4)
btnWindow4.grid(row=0,column=2,padx=5,pady=5,sticky=W)

btnWindow5=Button(window,text="Varesletting",command=window5)
btnWindow5.grid(row=0,column=3,padx=5,pady=5,sticky=W)

btnAvslutt=Button(window,text="Avslutt",command=window.destroy)
btnAvslutt.grid(row=1,column=4,padx=5,pady=5,sticky=W)

window.mainloop()
mindatabase.close()
varemarkor.close()
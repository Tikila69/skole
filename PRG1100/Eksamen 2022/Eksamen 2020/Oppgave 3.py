import mysql.connector
from tkinter import *


mindatabase=mysql.connector.connect(host='localhost', port=3306, user=' Bilsjef ', passwd='eksamen2020', db='Bildeling')

window=Tk()
window.title("Utleier ikke avsluttet")

def hentKundeinfo(event):
    valg=listeUtleie.get(listeUtleie.curselection())

    kundemarkor=mindatabase.cursor()
    kundemarkor.execute("SELECT Utleie.Regnr, Utleie.Utlevert, Utleie.Mobilnr, Kunde.Fornavn,Kunde.Etternavn FROM Utleie JOIN Kunde ON Utleie.mobilnr=Kunde.Mobilnr")


    
    for row in kundemarkor:
        if valg[0]==row[0]:
            mobilnr.set(row[2])
            fornavn.set(row[3])
            etternavn.set(row[4])

#Variabler
utleielisteInnhold=StringVar()
mobilnr=StringVar()
fornavn=StringVar()
etternavn=StringVar()

#Hente biler fra database til liste
bilmarkor=mindatabase.cursor()
bilmarkor.execute("SELECT Regnr, Utlevert FROM Utleie WHERE Innlevert IS NULL")

utleieliste=[]
for row in bilmarkor:
    utleieliste+=[[row[0],row[1]]]
utleielisteInnhold.set(utleieliste)
bilmarkor.close()

#Listebox
yScroll=Scrollbar(window,orient=VERTICAL)
yScroll.grid(row=0,column=2,rowspan=10,padx=(0,100),pady=5,sticky=NS)
listeUtleie=Listbox(window,width=28,height=10,listvariable=utleielisteInnhold,yscrollcommand=yScroll.set)
listeUtleie.grid(row=0,column=1,rowspan=10,padx=(100,0),pady=5,sticky=E)
yScroll["command"]=listeUtleie.yview
listeUtleie.bind("<<ListboxSelect>>",hentKundeinfo)

#Leieinfo
lblMobilnr=Label(window,text="Mobilnr:")
lblMobilnr.grid(row=0,column=11,padx=5,pady=5,sticky=E)
entMobilnr=Entry(window,width=11,state="readonly",textvariable=mobilnr)
entMobilnr.grid(row=0,column=12,padx=5,pady=5,sticky=W)

lblFornavn=Label(window,text="Fornavn:")
lblFornavn.grid(row=1,column=11,padx=5,pady=5,sticky=E)
entFornavn=Entry(window,width=20,state="readonly",textvariable=fornavn)
entFornavn.grid(row=1,column=12,padx=5,pady=5,sticky=W)

lblEtternavn=Label(window,text="Etternavn")
lblEtternavn.grid(row=2,column=11,padx=5,pady=5,sticky=E)
entEtternavn=Entry(window,width=30,state="readonly",textvariable=etternavn)
entEtternavn.grid(row=2,column=12,padx=5,pady=5,sticky=W)

#Avslutt knapp
btnAvslutt=Button(window,text="Avslutt",command=window.destroy)
btnAvslutt.grid(row=11,column=12,padx=5,pady=5,sticky=E)

window.mainloop()
mindatabase.close()

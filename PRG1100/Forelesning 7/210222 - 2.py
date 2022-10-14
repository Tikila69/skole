import mysql.connector
from tkinter import *

def hent_prisoglager(event):
    valg=lstVarer.get(lstVarer.curselection())

    prisoglagerMarkor=mindatabase.cursor()
    prisoglagerMarkor.execute("SELECT Betegnelse, Pris, Antall FROM Vare")


    for row in prisoglagerMarkor:
        if valg==row[0]:
            pris.set(row[1])
            lager.set(row[2])
    prisoglagerMarkor.close()


mindatabase=mysql.connector.connect(host="localhost",port="3306",user="Lagersjefen2022",password="Lagerpw",db="heltnydatabase")

varemarkor=mindatabase.cursor()

varemarkor.execute("SELECT * FROM Vare")

varer=[]

for row in varemarkor:
    varer+=[row[1]]

window=Tk()
window.title("Varer")
yScroll=Scrollbar(window,orient=VERTICAL)
yScroll.grid(row=0,column=2,rowspan=10,padx=(0,100),pady=5,sticky=NS)

innholdListeVarer=StringVar()
lstVarer=Listbox(window,width=50,height=10,listvariable=innholdListeVarer,yscrollcommand=yScroll.set)
lstVarer.grid(row=0,column=1,rowspan=10,padx=(100,0),pady=5,sticky=E)
innholdListeVarer.set(tuple(varer))
yScroll["command"]=lstVarer.yview

lblPris=Label(window,text="Pris:")
lblPris.grid(row=0,column=3,padx=5,pady=5,sticky=E)
lblLager=Label(window,text="Antall:")
lblLager.grid(row=1,column=3,padx=5,pady=5,sticky=E)

pris=StringVar()
entPris=Entry(window,width=10,state="readonly",textvariable=pris)
entPris.grid(row=0,column=4,padx=5,pady=5,sticky=W)

lager=StringVar()
entLager=Entry(window,width=10,state="readonly",textvariable=lager)
entLager.grid(row=1,column=4,padx=5,pady=5,sticky=W)

lstVarer.bind("<<ListboxSelect>>",hent_prisoglager)

window.mainloop()

varemarkor.close()
mindatabase.close()
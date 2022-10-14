import mysql.connector
from tkinter import *

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

mindatabase=mysql.connector.connect(host="localhost",port="3306",user="root", password="Icastfireball20",db="heltnydatabase")

varemarkor=mindatabase.cursor()

varemarkor.execute("select Betegnelse from vare")

varer=[]


for row in varemarkor:
    varer+=[row[0]]



window=Tk()
window.title=("Varesletting")
Yscroll=Scrollbar(window,orient=VERTICAL)
Yscroll.grid(row=0,column=2,rowspan=10,padx=(0,100),pady=5,sticky=NS)

betegnelse=StringVar()
innholdListeVarer=StringVar()

listeVarer=Listbox(window,width=50,height=10,listvariable=innholdListeVarer,yscrollcommand=Yscroll.set)
listeVarer.grid(row=0,column=1,rowspan=10,padx=(100,0),pady=5,sticky=E)
innholdListeVarer.set(tuple(varer))
Yscroll["command"]=listeVarer.yview

listeVarer.bind("<<ListboxSelect>>", henteVare)

btnSlette=Button(window,text="Slett Vare",command=SletteVare)
btnSlette.grid(row=10,column=3,padx=5,pady=5,sticky=SW)

btnAvslutt=Button(window,text="Avslutt",command=window.destroy)
btnAvslutt.grid(row=10,column=4,padx=5,pady=5,sticky=E)


window.mainloop()
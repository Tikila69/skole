import mysql.connector
from tkinter import *

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

mindatabase=mysql.connector.connect(host="localhost",port="3306",user="root",password="Icastfireball20",db="heltnydatabase")

varemarkor=mindatabase.cursor()

varemarkor.execute("SELECT Betegnelse FROM Vare")

varer=[]

for row in varemarkor:
    varer+=[row[0]]



window=Tk()
window.title("Varebeholdning")

yScroll=Scrollbar(window,orient=VERTICAL)
yScroll.grid(row=0,column=2,rowspan=10,padx=(0,100),pady=5,sticky=NS)

innholdListeVarer=StringVar()
listVarer=Listbox(window,width=50,height=10,listvariable=innholdListeVarer,yscrollcommand=yScroll.set)
listVarer.grid(row=0,column=1,rowspan=10,padx=(100,0),pady=5,sticky=E)
innholdListeVarer.set(tuple(varer))
yScroll["command"]=listVarer.yview

lblVarebeholdning=Label(window,text="Nåværende varebeholdning")
lblVarebeholdning.grid(row=0,column=3,padx=5,pady=5,sticky=E)

lblVarebeholdningNy=Label(window,text="Ny varebeholdning")
lblVarebeholdningNy.grid(row=1,column=3,padx=5,pady=5,sticky=E)

varenavn=StringVar()
lagerholdning=StringVar()
entBeholdning=Entry(window,width=10,state="readonly", textvariable=lagerholdning)
entBeholdning.grid(row=0,column=4,padx=5,pady=5,sticky=E)

nyLagerbeholdning=StringVar()
entNyBeholdning=Entry(window,width=10,textvariable=nyLagerbeholdning)
entNyBeholdning.grid(row=1,column=4,padx=5,pady=5,sticky=E)

listVarer.bind("<<ListboxSelect>>",hentBeholdning)

btnLagre=Button(window,text="Lagre",command=lagreNyBeholdning)
btnLagre.grid(row=6,column=3,padx=5,pady=5,sticky=E)

btnAvslutt=Button(window,text="Avslutt",command=window.destroy)
btnAvslutt.grid(row=6,column=4,padx=5,pady=5,sticky=E)

window.mainloop()

varemarkor.close()
mindatabase.close()
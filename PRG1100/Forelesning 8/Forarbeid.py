from cProfile import label
import mysql.connector
from tkinter import *

mindatabase=mysql.connector.connect(host="localhost",port="3306",user="root", password="Icastfireball20",db="heltnydatabase")

window=Tk()
window.title("Nye Varer")

lblVarebr=Label(window,text="Oppgi varenr: ")
lblVarebr.grid(row=0,column=0,padx=5,pady=5,sticky=E)
lblVarenavn=Label(window,text="Oppgi varenanv: ")
lblVarenavn.grid(row=1,column=0,padx=5,pady=5,sticky=E)
lblPris=Label(window,text="Oppgi pris: ")
lblPris.grid(row=2,column=0,padx=5,pady=5,sticky=E)
lblkatnr=Label(window,text="Oppgi Kategorinr: ")
lblkatnr.grid(row=3,column=0,padx=5,pady=5,sticky=E)
lblantall=Label(window,text="Oppgi antall: ")
lblantall.grid(row=4,column=0,padx=5,pady=5,sticky=E)
lblhylle=Label(window,text="Oppgi hylleplassering: ")
lblhylle.grid(row=5,column=0,padx=5,pady=5,sticky=E)

vnr=StringVar()
entVnr=Entry(window,width=6,textvariable=vnr)
entVnr.grid(row=0,column=1,padx=5,pady=5,sticky=W)
vnavn=StringVar()
entVnavn=Entry(window,width=20,textvariable=vnavn)
entVnavn.grid(row=1,column=1,padx=5,pady=5,sticky=W)
vpris=StringVar()
entVpris=Entry(window,width=5,textvariable=vpris)
entVpris.grid(row=2,column=1,padx=5,pady=5,sticky=W)
vkatnr=StringVar()
entVkatnr=Entry(window,width=4,textvariable=vkatnr)
entVkatnr.grid(row=3,column=1,padx=5,pady=5,sticky=W)
vantall=StringVar()
entVantall=Entry(window,width=4,textvariable=vantall)
entVantall.grid(row=4,column=1,padx=5,pady=5,sticky=W)
vhylle=StringVar()
entVhylle=Entry(window,width=4,textvariable=vhylle)
entVhylle.grid(row=5,column=1,padx=5,pady=5,sticky=W)

btnLagre=Button(window,text="Lagre")
btnLagre.grid(row=6,column=2,padx=5,pady=5,sticky=W)

window.mainloop()

mindatabase.close()

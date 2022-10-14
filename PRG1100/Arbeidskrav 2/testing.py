from tkinter import *
import mysql.connector

mindatabase=mysql.connector.connect(host="localhost",port="3306",user="Eksamenssjef",passwd="oblig2022",db="oblig2022")


def hentdato():
    hentemarkor=mindatabase.cursor()
    hdato=dato.get()

    print(hdato)

    

vindu=Tk()
vindu.title("Tester")

dato=StringVar()
funnet=StringVar()

lbldato=Label(vindu,text="Dato")
lbldato.grid(row=0,column=0,padx=5,pady=5)
entdato=Entry(vindu,width=8,textvariable=dato)
entdato.grid(row=0,column=1,padx=5,pady=5)

btnFinn=Button(vindu,text="Finn",command=hentdato)
btnFinn.grid(row=1,column=1,padx=5,pady=5)

entFunnet=Entry(vindu,width=10,textvariable=funnet)
entFunnet.grid(row=2,column=0,padx=5,pady=5)



vindu.mainloop()
mindatabase.close()
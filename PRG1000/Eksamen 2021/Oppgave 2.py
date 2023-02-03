from tkinter import *

#Definere programmet bak GUI
def foreleggskalkulator():
    fartsgrense=70
    din_fart=int(fart.get())
    if din_fart>=(fartsgrense+35):
        forelegg.set(9950)
    else:
        if din_fart>=(fartsgrense+25):
            forelegg.set(6250)
        else:
            if din_fart>=(fartsgrense+15):
                forelegg.set(3300)
            else:
                if din_fart>=(fartsgrense+5):
                    forelegg.set(750)
                else:
                    forelegg.set('Ingen forelegg')

#Definere vindu
window=Tk()

window.title('Foreleggskalulator')

#Første rad
#Definere label
lblDinFart=Label(window,text='Din fart:')
lblDinFart.grid(row=0,column=0,padx=15,pady=15)
#Definere input
fart=StringVar()
entDinFart=Entry(window,width=15,textvariable=fart)
entDinFart.grid(row=0,column=1,padx=15,pady=15)
#Definere knapp for kjøring av foreleggskalkulatorkalkulator
btnBeregnForelegg=Button(window,text='Beregn Forelegg',command=foreleggskalkulator)
btnBeregnForelegg.grid(row=0,column=2,columnspan=2,padx=15,pady=15)

#Andre rad
#Definere label
lblForelegg=Label(window,text='Forelegg:')
lblForelegg.grid(row=1,column=0,padx=15,pady=15)
#Defienre output
forelegg=StringVar()
entForelegg=Entry(window,width=20,state='readonly',textvariable=forelegg)
entForelegg.grid(row=1,column=1,padx=15,pady=15)

#Tredje rad
#Definere knapp for avslutting av program
btnAvslutt=Button(window,text='Avslutt',command=window.destroy)
btnAvslutt.grid(row=2,column=2,padx=15,pady=15)

window.mainloop()
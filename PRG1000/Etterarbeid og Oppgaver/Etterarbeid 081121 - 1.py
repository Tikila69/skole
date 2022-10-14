from tkinter import *

window=Tk()

def boliglanKalkulator():
    pris=int(prisKalkulator.get())
    inntekt=int(inntektKalkulator.get())
    egenkapital=int(egenkapitalKalkulator.get())

    lanesum=pris-egenkapital
    nodvendigEgenkapital=pris*0.15
    nodvendigInntekt=lanesum/5
    print('Det faktiske lånet vil komme på:',lanesum)
    print('Nødvendig Egenkapital for dette lånet er:',nodvendigEgenkapital)
    print('Nødvendig Inntekt for dette lånet er:',nodvendigInntekt)

    if egenkapital<nodvendigEgenkapital:
        resultat.set('Lån ikke innvilget')
    else:
        if inntekt<nodvendigInntekt:
            resultat.set('Lån ikke innvilget')
        else:
            if inntekt>=nodvendigInntekt and egenkapital>=nodvendigEgenkapital:
                resultat.set('Lånet er innvilget')

window.title('Boligåns kalkulator')

lblPris=Label(window,text='Oppgi pris på bolig')
lblInntekt=Label(window,text='Oppgi din inntekt')
lblEgenkapital=Label(window,text='Oppgi din egenkapital')

prisKalkulator=StringVar()
inntektKalkulator=StringVar()
egenkapitalKalkulator=StringVar()
resultat=StringVar()

entPris=Entry(window,width=8,textvariable=prisKalkulator)
entInntekt=Entry(window,width=7,textvariable=inntektKalkulator)
entEgenkapital=Entry(window,width=7,textvariable=egenkapitalKalkulator)

lblPris.grid(row=0,column=0,padx=100,pady=15)
lblInntekt.grid(row=1,column=0,padx=100,pady=15)
lblEgenkapital.grid(row=2,column=0,padx=100,pady=15)

entPris.grid(row=0,column=2,padx=100,pady=15)
entInntekt.grid(row=1,column=2,padx=100,pady=15)
entEgenkapital.grid(row=2,column=2,padx=100,pady=15)

btnBeregn=Button(window,text="Beregn",command=boliglanKalkulator)
btnBeregn.grid(row=3,columnspan=3,pady=15)

lblResultat=Label(window,text="Resultat")
lblResultat.grid(row=4,column=0,padx=100,pady=15)

entResultat=Entry(window,width=20,state="readonly",textvariable=resultat)
entResultat.grid(row=4,column=2,pady=15)

btnAvslutt=Button(window,text="Avslutt",command=window.destroy)
btnAvslutt.grid(row=5,columnspan=3,pady=15)


window.mainloop()
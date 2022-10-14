def marginalskattkalkulator():
    lonnsinntekt=int(inntekt.get())

    if lonnsinntekt>=964801:
        marginalskatt.set(46.4)
    else:
        if lonnsinntekt>=617501:
            marginalskatt.set(43.4)
        else:
            if lonnsinntekt>=245651:
                marginalskatt.set(34.4)
            else:
                if lonnsinntekt>=224001:
                    marginalskatt.set(32.1)
                else:
                    if lonnsinntekt>=174501:
                        marginalskatt.set(22.2)
                    else:
                        if lonnsinntekt>=102819:
                            marginalskatt.set(20.3)
    if lonnsinntekt<102819:
        marginalskatt.set('N/A')



from tkinter import *

window=Tk()

window.title('Marginalskattkalkulator')

lblLonnsinntekt=Label(window,text=('Lønnsinntekt:'))
lblLonnsinntekt.grid(row=0,column=0,padx=15,pady=15)

inntekt=StringVar()
entLonnsinntekt=Entry(window,width=8,textvariable=inntekt)
entLonnsinntekt.grid(row=0,column=1,padx=15,pady=15)

btnBeregn=Button(window,text=('Beregn marginalskattprosent'),command=marginalskattkalkulator)
btnBeregn.grid(row=0,column=2,columnspan=3,padx=15,pady=15)

lblMarginalskatt=Label(window,text=('Marginalskatt:'))
lblMarginalskatt.grid(row=1,column=0,padx=15,pady=15)

marginalskatt=StringVar()
entMarginalskatt=Entry(window,state='readonly',width=4,textvariable=marginalskatt)
entMarginalskatt.grid(row=1,column=1,padx=15,pady=15)

btnAvslutt=Button(window,text=('Avslutt'),command=window.destroy)
btnAvslutt.grid(row=2,column=4,padx=15,pady=15)

window.mainloop()

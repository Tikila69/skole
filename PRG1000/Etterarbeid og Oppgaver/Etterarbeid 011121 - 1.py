#Introduksjon til GUI programmering
#Grunnstruktur
#Med komponentene ledetekst, inndatafelt, utdatafelt og knapp
#Så legger vi å kode for å foreta "beregningene"
#Variable må knyttes til inndatafeltene og utdatafeltene, før plassering i grid
#Lager en avslutt knapp for å slippe å bruke "lukk vindu"

from tkinter import *

def beregnLan():
    ek=int(egenkapital.get())
    ks=int(kjopesum.get())
    if (ek/ks)>=0.35:
        lanetilsagn.set('Lån invilges')
    else:
        lanetilsagn.set('Lån invilges ikke')


window=Tk()

#Vi gir vinduet ett navn
window.title('Lånekalkulator billån')

#Vi lager ledetekster for kjøpesum, egekapital og lånetilsagn
lbl_kjopesum=Label(window,text='Kjøpesum')
lbl_kjopesum.grid(row=0, column=0, padx=100, pady=15)

lbl_egenkapita=Label(window,text='Egenkapital')
lbl_egenkapita.grid(row=1,column=0, padx=100, pady=15)

lbl_lanetilsagn=Label(window,text='Lånetilsagn')
lbl_lanetilsagn.grid(row=3,column=0,padx=100,pady=15)


#Vi lager inndatafelt for kjøpesum og egenkapital
kjopesum=StringVar()
ent_kjopesum=Entry(window,width=9,textvariable=kjopesum)
ent_kjopesum.grid(row=0,column=1,padx=100,pady=15)

egenkapital=StringVar()
ent_egenkapital=Entry(window,width=9,textvariable=egenkapital)
ent_egenkapital.grid(row=1,column=1,padx=100,pady=15)

#Vi lager knapp for å beregne lånetilsagnet
btn_beregn=Button(window,text='Beregn lånetilsagn',command=beregnLan)
btn_beregn.grid(row=2,column=0,columnspan=2,pady=15)

#Og vi lager et utdatafeilt/visningsfelst for konklusjonen på lånetilsagnet
lanetilsagn=StringVar()
ent_lanetilsagn=Entry(window,width=20,state='readonly',textvariable=lanetilsagn)
ent_lanetilsagn.grid(row=3,column=1,padx=100,pady=15)

#Knapp for å avslutte
btnAvslutt=Button(window,text='Avslutt',command=window.destroy)
btnAvslutt.grid(row=5,column=0,columnspan=2,pady=15)

window.mainloop()

#Arbeidsliste:
#1) Samle definisjoner av ledetext, komponent og variabel for de som hører sammen
#2) Bruke lokale variable på "get"-ere og "set"-ere.
#ek=int(egenkapital.get())
#3) Lage GUI-basert grensesnitt på (enkle) programmer med beregninger fra tidligere i høst
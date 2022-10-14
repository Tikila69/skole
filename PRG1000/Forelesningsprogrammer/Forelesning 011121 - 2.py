#Introduksjon til GUI programmering
#Grunnstruktur
#Med komponentene ledetekst, inndatafelt, utdatafelt og knapp

from tkinter import *
from typing import Collection
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

window.mainloop()


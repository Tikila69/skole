from tkinter import *

def bmiKalkulator():
    fortsette=True
    while fortsette==True:
        navn=input('Oppgi navn: ')
        hoydeMeter=float(input('Oppgi høyde i meter: '))
        vektKg=float(input('Oppgi vekt: '))

        def bmiKalkulater(navn,hoydeMeter,vektKg):
            bmi=vektKg/(hoydeMeter**2)
            print('BMI: ')
            print(bmi)
            print()
            if bmi<=25:
                return navn+' er ikke overvektig'
            else:
                return navn+' er overvektig'

        result=bmiKalkulater(navn,hoydeMeter,vektKg)

        print(result)
        print()
        print('Ønsker du å forsette programmet?')
        lokke=input('(j/n)')
        if lokke=="j":
            fortsette=True
        else:
            fortsette=False
    



window=Tk()
window.title('BMI Kalkulator')

lblNavn=Label(window,text="Navn",)
lblNavn.grid(window,row=0,column=0,padx=100,pady=15)
entNavn=Entry(window,textvariable)





window.mainloop()
#Definere variabler
lenge1=int(input('Definer lengden på det første rektangelet: '))
bredde1=int(input('Definer bredden på det første rektangelet: '))
lenge2=int(input('Definer lengden på den andre rektangelet: '))
bredde2=int(input('Definer bredden på det andre rektangelet: '))

areal1=lenge1*bredde1
areal2=lenge2*bredde2

if areal1>areal2:
    print('Det første rektangelet har et areal på',areal1,'og er det største rektangelet')
else:
    if areal2>areal1:
        print('Det andre rektangelet har et areal på',areal2,'og er det største rektangelet')
    else:
        print('Begge rektanglene er like store og har et areal på',areal1)
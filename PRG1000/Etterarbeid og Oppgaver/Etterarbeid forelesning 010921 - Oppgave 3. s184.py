#Definere bruker input
maned=int(input('Skriv måned som ett tall mellom 1 og 12: '))

#Finne korrekt kvartal for måned
if maned>9:
    print('Måneden er i 4. kvartal')
else:
    if maned>6:
        print('Måneden er i 3. kvartal')
    else:
        if maned>3:
            print('Måneden er i 2. kvartal')
        else:
            print('Måneden er i 1. kvartal')
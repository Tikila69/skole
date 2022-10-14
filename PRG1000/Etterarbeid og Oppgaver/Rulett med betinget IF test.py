#Be om input fra bruker
tall=int(input('Definer et tall mellom 0 og 36: '))

#Bruke if statements for å finne korrekt respons
if tall<0:
    print('Tallet er utenfor godkjent verdi. Prøv igjen med et annet tall')
else:
    if tall==0:
        print('Tallet',tall,'har grønn lomme')
    else:
        if tall>36:
            print('Tallet',tall,'er utenfor godkjent verdi. Prøv igjenmed et annet tall')
        else:
            if tall>=29:
                if tall%2==0:
                    print('Tallet',tall,'har rød lomme')
                else:
                    print('Tallet',tall,'har svart lomme')
            else:
                if tall>=19:
                    if tall%2==0:
                        print('Tallet',tall,'har svart lomme')
                    else:
                        print('Tallet',tall,'har rød lomme')
                else:
                    if tall>=11:
                        if tall%2==0:
                            print('Tallet',tall,'har rød lomme')
                        else:
                            print('Tallet',tall,'har svart lomme')
                    else:
                        if tall>=1:
                            if tall%2==0:
                                print('Tallet',tall,'har svart lomme')
                            else:
                                print('Tallet',tall,'har rød lomme')
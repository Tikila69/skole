#Få input fra pruker
tall=int(input('Skriv ett tall mellom 1 og 10: '))

#Konverter til romerske tall med IF statements
if tall<1:
    print('Error! Tallet er utenfor godtatt rekkevidde')
else:
    if tall==1:
        print('Tallet',tall,'konvertert til romerske tall er "I"')
    else:
        if tall==2:
            print('Tallet',tall,'konvertert til romerske tall er "II"')
        else:
            if tall==3:
                print('Tallet',tall,'konvertert til romerske tall er "III"')
            else:
                if tall==4:
                    print('Tallet',tall,'konvertert til romerske tall er "IV"')
                else:
                    if tall==5:
                        print('Tallet',tall,'konvertert til romerske tall er "V"')
                    else:
                        if tall==6:
                            print('Tallet',tall,'konvertert til romerske tall er "VI"')
                        else:
                            if tall==7:
                                print('Tallet',tall,'konvertert til romerske tall er "VII"')
                            else:
                                if tall==8:
                                    print('Tallet',tall,'konvertert til romerske taller "VIII"')
                                else:
                                    if tall==9:
                                        print('Tallet',tall,'konvertert til romerske tall er "IX"')
                                    else:
                                        if tall==10:
                                            print('Tallet',tall,'konvertert til romerske tall er "X"')
                                        else:
                                            if tall>10:
                                                print('Error! Tallet er utenfor godtatt rekkevidde')
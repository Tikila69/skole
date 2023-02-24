def  dekksett_for_kunde():
    sok=True
    while sok==True:
        mobilnr=input('Oppgi mobilnr: ')

        liste=[]

        kundefil=open('kunde.txt','r')
        dekksettfil=open('dekksett.txt','r')

        kundesok=kundefil.readline()
        while kundesok!='':
            fornavn=kundefil.readline()
            etternavn=kundefil.readline()
            epost=kundefil.readline()
            if kundesok.rstrip('\n')==mobilnr:
                liste+=[etternavn.rstrip('\n')]+[epost.rstrip('\n')]
            
                dekksok=dekksettfil.readline()
                while dekksok!='':
                    regnr=dekksettfil.readline()
                    if dekksok.rstrip('\n')==mobilnr:
                        liste+=[regnr.rstrip('\n')]
                    dekksok=dekksettfil.readline()
            kundesok=kundefil.readline()
        print(liste)
        fortsette=input('Ønsker du å foreta ett nytt søk? (j/n): ')
        if fortsette!='j':
            sok=False

dekksett_for_kunde()
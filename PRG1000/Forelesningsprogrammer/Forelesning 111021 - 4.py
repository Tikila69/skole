#Program for å skrive 3 nye navn til en eksisterende fil

#Åpne fila
studentfil=open('studentfil.txt','a')

#Lese inn 3 nye navn til fila
studentfil.write('Olivia\n')
studentfil.write('Oline\n')
studentfil.write('Petrus\n')

#stenge filen
studentfil.close()
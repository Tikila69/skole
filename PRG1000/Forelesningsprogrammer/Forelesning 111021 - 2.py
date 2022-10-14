#Program for å skrive 3 navn til 1 ny fil

#Definere og åpne fila student.txt
studentfil=open('studentfil.txt','w')

#Skriver 3 navn til fila
#Hver tekststreng slutter med \n
studentfil.write('Torvald\n')
studentfil.write('Kari\n')
studentfil.write('Jens\n')

#Stenger fila
studentfil.close()
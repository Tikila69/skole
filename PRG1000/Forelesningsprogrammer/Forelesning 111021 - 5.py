#Program for å lese en fil navn for navn og skrive ut de navnene som passer med søkekriteriene
#Generell fremgangsmåte jfr. fig 6-17 og program 6-9

#Åpner fila studentfil.txt
studentfil=open('studentfil.txt','r')

#Leser første linje i fila
#Ved bruk av readline-metoden
student=studentfil.readline()

#I python, readline returnerere en tom streng ('') når den leser EOF (end of file) -merket
#da tester vi på det

while student!='':
    if student[0]=='O':
        print(student.rstrip('\n'))
    #lese neste linje i fila
    student=studentfil.readline()

#Stenge fila
studentfil.close()

#Prøv selv: ta bort linjeskift (.rstrip)
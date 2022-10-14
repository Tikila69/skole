#Leser poster fra fil (uten og med rstrip)

studentfil=open('studentene.txt','r')

#Leser første linke/første felt i første post
studentnr=studentfil.readline()

while studentnr!='':
    studentnr=studentnr.rstrip('\n')
    #Leser resten av posten
    #Leser inn fornavn og studium og strip i en operasjon
    fornavn=studentfil.readline().rstrip('\n')
    studium=studentfil.readline().rstrip('\n')

    #Skriver ut posten
    print(studentnr,fornavn,studium)

    #Leser studentnr til neste studfent
    studentnr=studentfil.readline()

studentfil.close()
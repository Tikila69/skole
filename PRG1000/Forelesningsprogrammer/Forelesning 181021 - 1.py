# Legge poster til fil (variabel + '\n')

nyStudent= 'j'
studentfil=open('studentene.txt','a')

while nyStudent=='j':
    #Tar imot opplysninger om studenten
    studentnr=input('Oppgi studentnr: ')
    fornavn=input('Oppgi fornavn: ')
    studium=input('Oppgi studium: ')

    #Skriver studentopplynsingene til fil
    studentfil.write(studentnr+'\n')
    studentfil.write(fornavn+'\n')
    studentfil.write(studium+'\n')

    #legge til ny student?
    nyStudent=input('Vil du legge til ny student (j/n)? ')

studentfil.close()
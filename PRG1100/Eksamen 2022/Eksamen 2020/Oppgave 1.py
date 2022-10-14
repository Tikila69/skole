import mysql.connector

mindatabase=mysql.connector.connect(host='localhost', port=3306, user=' Bilsjef ', passwd='eksamen2020', db='Bildeling')

kundemarkor=mindatabase.cursor()

kundemarkor.execute("SELECT Mobilnr, Fornavn, Etternavn FROM Kunde")

kunder=[]
for row in kundemarkor:
    kunder+=[[row[0],row[1],row[2]]]

kundemarkor.close()
mindatabase.close()

print(kunder)


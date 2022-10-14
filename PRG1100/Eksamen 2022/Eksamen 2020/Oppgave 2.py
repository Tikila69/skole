import mysql.connector

mindatabase=mysql.connector.connect(host='localhost', port=3306, user=' Bilsjef ', passwd='eksamen2020', db='Bildeling')

bilmarkor=mindatabase.cursor()

bilmarkor.execute("SELECT * FROM Bil")

billiste={}
for row in bilmarkor:
    billiste[row[0]]={"Merke":row[1],"Modell":row[2],"Startdato":row[3],"Posisjon":row[4]}
bilmarkor.close()

fortsette=True
while fortsette:
    valg=input("Oppgi regnr: ")
    print(billiste[valg]["Merke"],billiste[valg]["Modell"],billiste[valg]["Startdato"])

    print()
    fortsett=input("Ønsker du å søke opp en ny bil? (y/n) ")

    if fortsett=="n":
        fortsette=False

mindatabase.close()
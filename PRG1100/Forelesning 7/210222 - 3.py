import mysql.connector


mindatabase=mysql.connector.connect(host="localhost",port="3306",user="Lagersjefen2022",password="Lagerpw",db="heltnydatabase")

settinnMarkor=mindatabase.cursor()
markor=mindatabase.cursor()

settinnMarkor.execute("INSERT INTO Vare"
                        "(VNr, Betegnelse, Pris, KatNr, Antall, Hylle)"
                        "VALUES('8888','EndaEnTestvare',88.88, 888, 88, 'T88')")
mindatabase.commit()

markor.execute("SELECT * FROM Vare")

for row in markor:
    print(row)

settinnMarkor.close()
markor.close()

mindatabase.close()


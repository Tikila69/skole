import mysql.connector


mindatabase=mysql.connector.connect(host="localhost",port="3306",user="Lagersjefen2022",password="Lagerpw",db="heltnydatabase")

settinnMarkor=mindatabase.cursor()
markor=mindatabase.cursor()

varenr=input("Oppgi varenr: ")
varenavn=input("Oppgi varenavn: ")
pris=float(input("Oppgi pris: "))
katnr=int(input("Oppgi kategorinr: "))
antall=int(input("Oppgi antall: "))
hylle=input("Oppgi gylleplassering: ")

settinnMarkor.execute("INSERT INTO Vare"
                        "(VNr, Betegnelse, Pris, KatNr, Antall, Hylle)"
                        "Values('9999','Testvare',99.99,999,99,'T99')")

mindatabase.commit()
settinVare=("INSERT INTO Vare"
            "(Vnr, Betegnelse, Pris, KatNr, Antall, Hylle)"
            "VALUES(%s,%s,%s,%s,%s,%s)")
dataNyVare=(varenr,varenavn,pris,katnr,antall,hylle)

settinnMarkor.execute(settinVare,dataNyVare)
mindatabase.commit()

markor.execute("SELECT * FROM Vare")

for row in markor:
    print(row)

settinnMarkor.close()
markor.close()

mindatabase.close()
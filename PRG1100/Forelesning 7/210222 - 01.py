import mysql.connector

mindatabase=mysql.connector.connect(host="localhost",port="3306",user="Lagersjefen2022",passwd="Lagerpw",db="heltnydatabase")


markor=mindatabase.cursor()

markor.execute("SELECT * FROM Vare")

for row in markor:
    print(row)


markor.close()

mindatabase.close()

import mysql.connector

def hae_maakoodilla(mkoodi):
    sql = f"SELECT type, COUNT(*) FROM airport WHERE iso_country='{mkoodi}' GROUP BY type ORDER BY COUNT(*) DESC"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    print(tulos)
    return

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='jyrki',
         password='salasana',
         autocommit=True
         )

maakoodi = input("Anna maakoodi: ")
hae_maakoodilla(maakoodi)
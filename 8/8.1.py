import mysql.connector

def hae_ICAO_koodilla(ICAO):
    sql = f"SELECT name, municipality FROM airport WHERE ident='{ICAO}'"
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

ICAO = input("Anna ICAO-koodi: ")
hae_ICAO_koodilla(ICAO)
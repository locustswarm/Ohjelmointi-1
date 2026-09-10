import mysql.connector
from geopy.distance import geodesic

def hae_ICAO_koodilla(ICAO1, ICAO2):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident='{ICAO1}'"
    sql2 = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident='{ICAO2}'"

    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos1 = kursori.fetchall()
    kursori.execute(sql2)
    tulos2 = kursori.fetchall()

    distance = geodesic(tulos1, tulos2).km
    print(f"Lentokenttien etäisyys on {int(distance)} kilometriä")
    return

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='jyrki',
         password='salasana',
         autocommit=True
         )

ICAO1 = input("Anna ensimmäinen ICAO-koodi: ")
ICAO2 = input("Anna toinen ICAO-koodi: ")
hae_ICAO_koodilla(ICAO1,ICAO2)
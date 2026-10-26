class Julkaisu:

    def __init__(self, julkaisu):
        self.julkaisu = julkaisu

    def tulostatiedot(self):
        print(self.julkaisu)

class Kirja(Julkaisu):
    def __init__(self, julkaisu, kirjailija, sivut):
        self.kirja = kirjailija
        self.sivut = sivut
        super().__init__(julkaisu)

    def tulostatiedot(self):
        super().tulostatiedot()
        print(f"Kirjailija: {self.kirja}\nSivujen määrä: {self.sivut}")

class Lehti(Julkaisu):
    def __init__(self, julkaisu, ptoimittaja):
        self.ptoimittaja = ptoimittaja
        super().__init__(julkaisu)

    def tulostatiedot(self):
        super().tulostatiedot()
        print(f"Päätoimittaja: {self.ptoimittaja}\n")

aku = Lehti("Aku Ankka", "Aki Hyyppä")
aku.tulostatiedot()

hytti = Kirja("Hytti n:o 6", "Rosa Liksom", "200")
hytti.tulostatiedot()

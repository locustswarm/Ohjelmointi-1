class Auto:
    nopeusnyt = 0
    kuljettumatka = 0
    def __init__(self, rtunnus, hnopeus):
        self.rtunnus = rtunnus
        self.hnopeus = hnopeus
    def kiihdyta(self, kmh):
        if Auto.nopeusnyt + kmh < 0:
            Auto.nopeusnyt = 0
        elif Auto.nopeusnyt + kmh > self.hnopeus:
            Auto.nopeusnyt = self.hnopeus
        else:
            Auto.nopeusnyt = Auto.nopeusnyt + kmh
    def kulje(self, kmh):
        Auto.kuljettumatka += Auto.nopeusnyt * kmh

auto1 = Auto('ABC-123', 142)
print(f"Auton rekisteri tunnus on: {auto1.rtunnus} "
      f"\nHuippunopeus on: {auto1.hnopeus}"
      f"\nTämän hetkinen nopeus on: {auto1.nopeusnyt}"
      f"\nKuljettu matka on: {auto1.kuljettumatka} km")
auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)
print(f"\nTämän hetkinen nopeus on: {auto1.nopeusnyt} ")
auto1.kiihdyta(-200)
print(f"Hätäjarrutus: {auto1.nopeusnyt} ")
auto1.kiihdyta(60)
auto1.kulje(1.5)
print(f"\nKuljettu matka on: {auto1.kuljettumatka} km")
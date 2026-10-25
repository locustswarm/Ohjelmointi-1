class Auto:
    nopeusnyt = 0
    kuljettumatka = 0
    def __init__(self, rtunnus, hnopeus):
        self.rtunnus = rtunnus
        self.hnopeus = hnopeus

auto1 = Auto('ABC-123', 142)
print(f"Auton rekisteri tunnus on: {auto1.rtunnus} "
      f"\nHuippunopeus on: {auto1.hnopeus}"
      f"\nTämän hetkinen nopeus on: {auto1.nopeusnyt}"
      f"\nKuljettu matka on: {auto1.kuljettumatka} km")
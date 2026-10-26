class Hissi:
    moneskohissi = 1
    def __init__(self, alin, ylin):
        self.kerros = alin
        self.alin = alin
        self.ylin = ylin
        self.hissinro = Hissi.moneskohissi
        Hissi.moneskohissi += 1

    def siirry_kerrokseen(self, kerros):
        if kerros < self.kerros:
            for i in range (kerros, self.kerros):
                self.kerros_alas()
        else:
            for i in range (self.kerros, kerros):
                self.kerros_ylos()

    def kerros_alas(self):
        if self.kerros != self.alin:
            self.kerros -= 1
            print(f"Hissi{self.hissinro} on kerroksessa {self.kerros}")

    def kerros_ylos(self):
        if self.kerros != self.ylin:
            self.kerros += 1
            print(f"Hissi{self.hissinro} on kerroksessa {self.kerros}")

class Talo:
    def __init__(self, alin, ylin, hissit):
        self.alin = alin
        self.ylin = ylin
        self.hissit = []
        self.hissienmaara = hissit

    def hissienluonti(self):
        for i in range(1, self.hissienmaara+1):
            talonhissi = Hissi(self.alin, self.ylin)
            self.hissit.append(talonhissi)

    def ajahissia(self, hissinro, kerros):
        for hissi in self.hissit:
            if hissi.hissinro == hissinro:
                hissi.siirry_kerrokseen(kerros)

kivitalo = Talo(1,4, 3)
kivitalo.hissienluonti()
kivitalo.ajahissia(1, 10)


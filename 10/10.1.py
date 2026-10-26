class Hissi:
    def __init__(self, alin, ylin):
        self.kerros = alin
        self.alin = alin
        self.ylin = ylin
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
            print(f"Hissi on kerroksessa {self.kerros}")
    def kerros_ylos(self):
        if self.kerros != self.ylin:
            self.kerros += 1
            print(f"Hissi on kerroksessa {self.kerros}")

hissi = Hissi(1, 10)
hissi.siirry_kerrokseen(5)
hissi.siirry_kerrokseen(1)

import random

def noppa(tahkot):
    while True:
        luku = random.randint(1, tahkot)
        print(luku)
        if luku == tahkot:
            break

noppa(int(input('Anna tahkojen määrä: ')))
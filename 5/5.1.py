import random

heitot = int(input('Kuinka monta arpakuutioita: '))
summa = 0
for i in range(heitot):
    summa = summa + random.randint(1, 6)

print(summa)
#En tiedä saanko käyttää for-looppia, mutta käytän sitä silti
import random

koodi = ""

for i in range(3):
    koodi += str(random.randint(0,9))

print (koodi)

koodi = ""

for i in range(4):
    koodi += str(random.randint(1,6))

print(koodi)
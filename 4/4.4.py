from random import randint

arvattava = randint(1,10)
arvaus = int(input('Arvaa luku 1 ja 10 välillä: '))
while arvaus != arvattava:
    if arvaus > arvattava:
        print('Liian suuri arvaus')
    elif arvaus < arvattava:
        print('Liian pieni arvaus')
    arvaus = int(input('Arvaa luku 1 ja 10 välillä: '))
print('Oikein!')
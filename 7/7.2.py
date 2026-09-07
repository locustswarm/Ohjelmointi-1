nimi = input('Anna nimi: ')
nimet = set()

while nimi !='':
    nimi = input('Anna nimi: ')
    if nimi in nimet:
        print('Aiemmin syötetty nimi')
    else:
        print('Uusi nimi')
    nimet.add(nimi)

for i in nimet:
    print(i)
luku = (input('Anna luku: '))
pienin = luku
suurin = luku
while luku != "":
    if int(luku < pienin):
        pienin = luku
    elif int(luku > suurin):
        suurin = luku
    luku = (input('Anna luku: '))

print(f'Suurin antamasi luku oli: {suurin}\nPienin antamasi luku oli: {pienin}')
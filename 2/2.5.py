#Yksi leiviskä on 20 naulaa.
#Yksi naula on 32 luotia.
#Yksi luoti on 13,3 grammaa.

naulat = float(input('Anna leiviskät: ')) * 20
naulat += float(input('Anna naulat: '))
luodit = float(input('Anna luodit: '))

massa = (luodit + naulat * 32) * 13.3
kg = int(massa/1000)
g = massa - kg * 1000
print(massa)
print(f'Massa nykymittojen mukaan:\n'
      f'{int(massa/1000)} kilogrammaa ja {g:.2f} grammaa')
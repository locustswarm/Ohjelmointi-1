hytti = input('(LUX, A, B, C)\nMikä on hyttiluokkasi? ')

if hytti.upper() == 'LUX':
    print('LUX on parvekkeellinen hytti yläkannella')
elif hytti.upper() == 'A':
    print('A on ikkunallinen hytti autokannen yläpuolella')
elif hytti.upper() == 'B':
    print('B on ikkunaton hytti autokannen yläpuolella')
elif hytti.upper() == 'C':
    print('C on ikkunaton hytti autokannen alapuolella')
else:
    print('Virheellinen hyttiluokka')
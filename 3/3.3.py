spuoli = input('Oletko mies vai nainen? ')
hemoglob = int(input('Mikä on hemoglobiiniarvosi? '))

if spuoli.lower() == 'nainen':
    if hemoglob > 175:
        print('hemoglobiiniarvosi on korkea')
    elif hemoglob < 117:
        print('hemoglobiiniarvosi on alhainen')
    else:
        print('hemoglobiiniarvosi on normaali')
elif spuoli.lower() == 'mies':
    if hemoglob > 195:
        print('hemoglobiiniarvosi on korkea')
    elif hemoglob < 134:
        print('hemoglobiiniarvosi on alhainen')
    else:
        print('hemoglobiiniarvosi on normaali')
else:
    print('yritä uudelleen')

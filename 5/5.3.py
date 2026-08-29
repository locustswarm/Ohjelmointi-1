luku = int(input('Anna luku: '))
lista = []

for i in range (1,luku+1,1):
    for j in range (1,luku+1,1):
        if luku / j == i:
            lista.append(i)

if len(lista) == 2 and 1 in lista and luku in lista:
    print('Lukusi on alkuluku')
else:
    print('Lukusi ei ole alkuluku')
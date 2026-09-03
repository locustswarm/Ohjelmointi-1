def listansumma(lista):
    summa = 0
    for i in lista:
        summa += i
    return summa

luvut = [1,2,3,4,5]
tulos = listansumma(luvut)
print(tulos)
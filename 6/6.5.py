def karsittulista(lista):
    karsittu = lista.copy()
    for i in karsittu:
        if i % 2 != 0:
            karsittu.remove(i)
    return karsittu

luvut = [1,2,3,4,5,6,7,8,9,10]
tulos = karsittulista(luvut)
print(f'Alkuperäinen lista: {luvut}\nKarsittulista: {tulos}')
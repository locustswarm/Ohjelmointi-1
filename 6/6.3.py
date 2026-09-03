def muunnos(gallonat):
    litrat = gallonat * 3.785
    return litrat

while True:
    gallonat = int(input('Anna gallonat: '))
    if gallonat < 0:
        break
    print(muunnos(gallonat))
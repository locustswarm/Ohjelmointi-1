yritykset = 0

while yritykset < 5:
    ktunnus = input('Anna käyttäjätunnus: ')
    ssana = input('Anna salasana: ')
    if ktunnus == 'python' and ssana == 'rules':
        print('Tervetuloa')
        break
    else:
        print('Pääsy evätty')
        yritykset += 1

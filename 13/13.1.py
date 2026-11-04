from flask import Flask, Response

app = Flask(__name__)
@app.route('/alkuluku/<luku>')
def alkuluku(luku):
    lista = []
    luku = int(luku)
    for i in range(1, luku + 1, 1):
        for j in range(1, luku + 1, 1):
            if luku / j == i:
                lista.append(i)

    if len(lista) == 2 and 1 in lista and luku in lista:
        vastaus = {
            "Number": luku,
            "isPrime": True
        }
        return vastaus
    else:
        vastaus = {
            "Number": luku,
            "isPrime": False
        }
        return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
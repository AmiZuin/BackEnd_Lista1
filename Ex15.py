cont = 0
matriz = []

# Crivo de Eratóstenes
limite = 100
primos = [True] * (limite + 1)
primos[0] = primos[1] = False

for numero in range(2, int(limite**0.5) + 1):
    if primos[numero]:
        for multiplo in range(numero * numero, limite + 1, numero):
            primos[multiplo] = False
            

for i in range(10):
    linha = []
    for j in range(10):
        cont+=1
        linha.append(cont)
    matriz.append(linha)

for linha in matriz:
    for elemento in linha:
        marca = '*' if primos[elemento] else ' '
        print(f'{elemento}{marca}\t', end='')
    print()



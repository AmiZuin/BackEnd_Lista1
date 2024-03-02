import random

lin = 10
col = 10
matriz = []
matriz2 = []

for i in range(lin):
    linha = []
    for j in range(col):
        numero = random.randint(1, 20)
        linha.append(numero)
    matriz.append(linha)

print("Matriz 1:")

for linha in matriz: 
    print(linha)

print("")

for i in range(lin):
    linha2 = []
    for j in range(col):
        if i == j:
            linha2.append(1)
        if i < j:
            linha2.append(0)
        if i > j:
            linha2.append(2)
    matriz2.append(linha2)

print("Matriz 2:")

for linha2 in matriz2: 
    print(linha2)



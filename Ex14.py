lin = 3
col = 4

matriz = []
matriz_t = []

for i in range(lin):
    linha = []
    for j in range(col):
        numero = int(input("Digite os números da Matriz: "))
        linha.append(numero)
    matriz.append(linha)

print("")

print("Matriz")
for linha in matriz:
    print(linha)

print("")

transposta = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

print("Transposta da Matriz")
for linha in transposta:
    print(linha)

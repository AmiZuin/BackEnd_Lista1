lin = 3
col = 3
matriz = []

for i in range(lin):
    linha = []
    for j in range(col):
        num = int(input("Digite os números da Matriz: "))
        linha.append(num)
    matriz.append(linha)

print("")
print("Matriz")
for linha in matriz:
    print(linha)

def determinante(matriz):
    det = (matriz[0][0] * matriz[1][1] * matriz[2][2]) + \
          (matriz[0][1] * matriz[1][2] * matriz[2][0]) + \
          (matriz[0][2] * matriz[1][0] * matriz[2][1]) - \
          (matriz[2][0] * matriz[1][1] * matriz[0][2]) - \
          (matriz[2][1] * matriz[1][2] * matriz[0][0]) - \
          (matriz[2][2] * matriz[1][0] * matriz[0][1])
    
    return det

det = determinante(matriz)

print("")
print(f'O determinante da Matriz é: {det}')


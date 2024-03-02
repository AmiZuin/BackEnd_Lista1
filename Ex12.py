import random 

lista = []
qt = 0

for i in range(1, 1001):
    numero = random.randint(1, 2000)
    lista.append(numero)

for i in lista:
    if i >= 700:
        qt+=1

porcentagem = qt * 100 / len(lista)

print(f'A porcentagem dos números maiores ou iguais a 700 existentes no vetor é {porcentagem}%')
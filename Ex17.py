lista = []

for i in range(10):
    n = int(input("Digite os números: "))
    lista.append(n)

print("")
print("Lista Original: ", lista)

n = len(lista)
for i in range(n):
    for j in range(0, n-i-1):
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]

print("")
print("Lista Ordenado Crescente:", lista)


for i in range(n):
    for j in range(0, n-i-1):
        if lista[j] < lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]

print("")
print("Lista Ordenado Decrescente:", lista)
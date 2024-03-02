num = []
pares = []
impares = []
impar = 0
par = 0

for i in range(1,11):
    n = int(input("Digite um número: "))
    print("")
    num.append(n)

for i in num:
    if i % 2 != 0:
        impar += 1
        impares.append(i)
    else:
        par +=1
        pares.append(i)

soma_par = sum(pares)
media_impar = sum(impares) / len(impares)

print(f'Foram informados {par} números Pares.')
print(f'Foram informados {impar} números Ímpares.')
print(f'A soma dos números pares é {soma_par}')
print(f'A média dos números ímpares é {media_impar}')


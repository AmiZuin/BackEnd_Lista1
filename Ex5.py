n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

print("")

if n1 == n2 or n1 == 0 or n2 == 0:
    print("Os números devem ser diferentes e maiores que 0. Tente Novamente!")

else:
    if n1 < n2:
        menor = n1
        maior = n2

    else:
        menor = n2
        maior = n1

    maior+=1

    while menor < maior:
        for count in range(10):
            print("%d x %d = %d" % (menor, count+1, menor*(count+1)))
        menor+=1
        print("")
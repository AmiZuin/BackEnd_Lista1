mult = 0

n = int(input("Digite um número: "))
print("")

if n < 1:
    print("O número deve ser maior que 1. Tente novamente!")

else:
    for count in range(2, n):
        if n % count == 0:
            mult+=1

    if mult == 0:
        print(f'{n} é primo')
    
    else:
        print(f'{n} não é primo')


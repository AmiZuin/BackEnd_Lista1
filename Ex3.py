n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

print("")

print("Escolha uma opção: ")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")
escolha = str(input(""))

print("")

if escolha == "1":
    soma = n1 + n2
    print(f'O resultado da soma é: {soma}')

elif escolha == "2":
    subtracao = n1 - n2
    print(f'O resultado da soma é: {subtracao}')

elif escolha == "3":
    multiplicacao = n1 * n2
    print(f'O resultado da soma é: {multiplicacao}')

else:
    divisao = n1 / n2
    print(f'O resultado da soma é: {divisao}')
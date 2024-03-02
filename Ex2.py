altura = float(input("Digite a sua altura: "))
peso = float(input("Digite seu peso: "))

IMC = peso / (altura * altura)

print("")

if IMC < 16.5:
    print("Desnutrição")
    print(f'IMC: {IMC}.')

elif IMC > 16.6 and IMC < 18.5:
    print("Abaixo do peso")
    print(f'IMC: {IMC}.')

elif IMC > 18.6 and IMC < 24.9:
    print("Peso normal")
    print(f'IMC: {IMC}.')

elif IMC > 25 and IMC < 29.9:
    print("Sobrepeso")
    print(f'IMC: {IMC}.')

else:
    print("Obesidade")
    print(f'IMC: {IMC}.')
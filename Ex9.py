def calculo_fatorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * calculo_fatorial(numero - 1)
    
numero = int(input("Digite um número: "))
print("")

resultado = calculo_fatorial(numero)

print(f'O fatorial de {numero} é {resultado}')

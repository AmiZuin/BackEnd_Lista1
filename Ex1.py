cliente = str(input("Digite o seu nome: "))
endereco = str(input("Digite seu endereço: "))
valor_compras = float(input("Digite o valor da compra: "))
data_entrega = str(input("Digite a data de entrega (Ex: xx/xx/xxxx): "))

print("")

print(30*" " + "AVISO")
print(f'Caro cliente Sr(a) {cliente}, os produtos da sua compra no')
print(f'valor de R$ {valor_compras} serão entregues no endereço abaixo:')
print(f'Rua {endereco}.')
print(f'Data de entrega: {data_entrega}.')
print(" " + 20*"*" + " Obrigado pela Preferência! " + 20*"*")
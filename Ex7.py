import random

numero = random.randint(0,9)
tentativa = 0

print("Bem-vindo ao jogo de adivinhação! Será que você consegue acertar o número que a máquina separou? Veremos.")
print("Boa sorte jogador!")
print("")

print("Qual é o número de seu palpite? (Dica: o número sorteado está entre 0 e 9):")
chute = int(input(""))
print("")

while chute != numero:
    if chute != numero:
        tentativa += 1
        print("Errou! Tente novamente!")
        print("")

    else:
        print("Parabéns jogador você acertou!")
        print(f'O número sorteado era {numero}')
        print(f'Você realizou {tentativa} tentativas')

    print("Qual é o número de seu palpite? (Dica: o número sorteado está entre 0 e 9):")
    chute = int(input(""))
    print("")

if chute == numero:
    print("Parabéns jogador você acertou!")
    print(f'O número sorteado era {numero}')
    print(f'Você realizou {tentativa} tentativas')


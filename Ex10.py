from getpass import getpass

login = str(input("Login: "))
senha = getpass("Senha: ")

erro = 1

while erro != 3:
    if login == "IFSP" and senha == "PosWEB":
        print("Login efetuado com sucesso!")
        break

    else:
        erro += 1
        print("Senha incorreta!")
        print("")

    login = str(input("Login: "))
    senha = getpass("Senha: ")

if erro == 3:
    print("Acesso negado!")
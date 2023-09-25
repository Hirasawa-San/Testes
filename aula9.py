passw = '12345'
login = '50734'

print("Olá, Digite 'E' para logar ou digite 'S' para sair.")
opcao = input("")
opcaoc = opcao.upper
print(opcao)
if opcao == "E":
    print("Digite seu login:")
    logint = input('').upper
    if logint == login:
        print("Digite suaa senha:")
        passwordt = input("")
        if passwordt == passw:
            print(f"Bem vindo Usuário {login}")
        else:
            print("senha Invalida")
    else:
        print("Login invalido.")



elif opcao == "S":
    print("Você saiu.")
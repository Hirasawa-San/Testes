import csv

# definir a função de cadastro de usuário
def cadastrar_usuario(nome, email, senha):
    with open('usuarios.csv', mode='a', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([nome, email, senha])
    print("Usuário cadastrado com sucesso!")

# definir a função de login
def fazer_login(email, senha):
    with open('usuarios.csv', mode='r') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            if linha[1] == email and linha[2] == senha:
                print("Login realizado com sucesso!")
                return
        print("E-mail ou senha incorretos.")

# pedir ao usuário para escolher uma opção
opcao = input("Digite 'c' para cadastrar um novo usuário ou 'l' para fazer login: ")

if opcao == 'c':
    # pedir ao usuário para fornecer informações de cadastro
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")
    confirmacao_senha = input("Confirme sua senha: ")

    # verificar se as senhas coincidem
    if senha != confirmacao_senha:
        print("As senhas não coincidem.")
    else:
        cadastrar_usuario(nome, email, senha)

elif opcao == 'l':
    # pedir ao usuário para fornecer informações de login
    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")

    fazer_login(email, senha)

else:
    print("Opção inválida.")

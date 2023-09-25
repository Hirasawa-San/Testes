print("Hello", "world!", sep=", ") #O "sep" é utilizado para subtituir o separador (o padrão é o espaço " ")

# CRLF = /r/n
# CRLF é básicamente a quebra de linha do windows

print("The book is on the", "table", sep=" ", end=".\n") #O "end" é utilizado para substituir a forma que o print encerra (o padrão é \n\r)
name = ""
telefone = ""
email = ""
passw = ""
confpassw = ""
ano = 2023

try:
    name = input('Digite seu nome: ')
    email = input('Digite seu email: ')
    print('digite seu ano de nascimento:')
    years = input(int())
    passw = input('Digite sua senha: ')
    confpassw = input('Digite sua senha novamente: ')
    #if passw != confpassw:


except passw != confpassw:
    print("erro ao cadastrar, sua senha não confere") 
    exit()

print('Cadastro realizado com sucesso, bem-vindo', name,'\n')
print('Para acessar seus dados de cadasatro digite 1 \nPara sair digite 0')
option = input()
yearsa = int(ano) - int(years)
while True:
    if option == 'info':
        print('Dados de conta\n')
        print('Nome:', name)
        print('\nEmail:', email)
        print('Idade:',str(yearsa), 'anos')
        print('Senha: ', passw)
        exit()
    else:
        exit()

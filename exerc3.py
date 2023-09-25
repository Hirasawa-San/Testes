print("Olá, vamos iniciar seu cadastro")
print("\n")

nome = input("Digite aqui o seu nome completo: ")
idade = input("Digite aqui sua idade: ")

if nome and idade:
    invnome = nome[::-1]
    
    print(f'Seu nome é {nome}')
    print(f'Você possui {idade} anos de idade')
    print(f'Seu nome invertido ficaria assim: {invnome}')
    if " " in nome:
        print(f"Seu nome possui espaço(s)")
    else:
        print(f"Seu nome não possui espaços")
    print(f"Seu nome possui {len(nome)} caracteres")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A ultima letra do seu nome é {nome[-1]}")

else:
    print("Você deixou algum espaço vazio")
# Isso é um comentário (obvio)

'''
Isso aqui é um DoctString (não é um comentário)

Mas pode ser usado como um (melhor não)
'''
# Função para somar dois números
def soma(a, b):
    return a + b

# Função para subtrair dois números
def subtracao(a, b):
    return a - b

# Função para multiplicar dois números
def multiplicacao(a, b):
    return a * b

# Função para dividir dois números
def divisao(a, b):
    if b == 0:
        print("Erro: Divisão por zero!")
        return None
    else:
        return a / b

# Função para exibir o menu da calculadora
def menu():
    print("Escolha uma opção:")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 - Sair")

# Loop principal da calculadora
while True:
    menu()
    escolha = input("Opção: ")
    if escolha == '0':
        print("Saindo...")
        break
    
    # Lê os dois números da entrada padrão
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        resultado = soma(num1, num2)
        print("Resultado: ", resultado)
    elif escolha == '2':
        resultado = subtracao(num1, num2)
        print("Resultado: ", resultado)
    elif escolha == '3':
        resultado = multiplicacao(num1, num2)
        print("Resultado: ", resultado)
    elif escolha == '4':
        resultado = divisao(num1, num2)
        if resultado is not None:
            print("Resultado: ", resultado)
    else:
        print("Opção inválida")
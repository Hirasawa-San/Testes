# Conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# Tipos imútaveis e primitivos:
# str, int, float, bool
# Exemplo (Apesar de né?):
print("Olá, faça a sua soma agora!", end="\n \n")
num1 = input("digite o primeiro numero: ")
num2 = input("digite o segundo numero: ")

print(num1 + num2, "esse é o resultado sem o typecasting", end='\n \n')

print("Olá, faça a sua soma agora!", end="\n \n")

num4 = input("digite o primeiro numero: ")
num5 = input("digite o segundo numero: ")

print(int(num4) + int(num5), "e essse é o resultado com o typecasting")

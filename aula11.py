"""
Fatiamento de strings
 012345678
 Olá mundo
-123456789
Fatiamento [i:f:p] [::]
[inicio(por onde começar):final(aonde parar):passo(qual a sequencia)]
Obs.: a função len retorna a qtd
de caracteres da str
"""

variavel = "Olá mundo"
print(variavel[0::2]) # 

print(variavel[::-1]) # Utiliza-se números negativos para que a forma de exibição da string seja invertida 
print(variavel[-1:-10:-1]) # 

print(len(variavel)) # Função 'len' é utilizada para fazer a contagem de caracteres da string ou outro objeto
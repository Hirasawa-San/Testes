'''
Dica boa, coisa boa, joia viu python, obrigado microsoft
Utilize o comando "ctrl + barra" para comentar(ou descomentar(?)) automaticamente as linhas selecionadas
'''
"""
esquece, n funciona no meu F
"""

import random
#Define uma função que cria um peso para ordenar
def peso():
  return random.random()


lista = ['brouvee','soulswap','exodus','altermind']

random.shuffle(lista,peso)

print(lista[1])


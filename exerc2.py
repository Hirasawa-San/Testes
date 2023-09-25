name = input("Digite seu nome: ")
print("\n")

print("Digite sua altura (em metros):", end="")
alt = input()
print('\n')

print("Digite seu peso (em KG):", end="")
pes = input()
print('\n')

try:
    
    imc = float(pes) / (float(alt) * float(alt))
    #F-string exemplo (não foca mt nisso não que vai ter uma aula focada nesse assunto)
    print(f'{name} \nSeu peso é {str(pes)} \nSua altura e {str(alt)}\nE seu IMC é: {imc:.2}')

except:
    print("ouve erro ao processar os dados.")
    

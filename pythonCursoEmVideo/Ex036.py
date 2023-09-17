'''
programa que lei um numero inteiro qualquer
peça para o usuário escolher qual será a base de conversão
1 para binário
2 para octal
3 para hexadecimal
'''

print("1- Vasco")
print("2- Vasco da Gama")
print("3- Gigante da Colina")
num = int(input("Digite um número e faça a sua escolha: "))

if num == 1:
    print(f"Você escolhe o número {num}")
    print("Vasco!")
elif num == 2:
    print(f"Você escolhe o número {num}")
    print("Vasco da gamma!")
elif num == 3:
    print(f"Você escolhe o número {num}")
    print("Gigante da colina!")
else:
    print("Opção inexistente!")
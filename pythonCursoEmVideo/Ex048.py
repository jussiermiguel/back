"""
refaça o desafio 009
mostrando a tabuada de um número que o usuário escolher
utilizando for
"""

num = int(input("Digite um número para ver a sua tabuada completa: "))
print('-' * 20)
print("SOMA!")
for i in range(1,11):
    print(f"{num} + {i} = {num+i}")
print('-' * 20)

print("SUBTRAÇÃO!")
for i in range(1,11):
    print(f"{i} - {num} = {i-num}")
print('-' * 20)

print("MULTIPLICAÇÃO!")
for i in range (1, 11):
    print(f"{num} * {i} = {num*i}")
print('-' * 20)

print("DIVISÃO!")
for i in range (1, 11):
    print(f"{i} / {num} = {num / i}")
print('-' * 20)
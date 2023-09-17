"""
leia um número
diga se ele é primo ou não
"""

num = int(input("Digite um número para saber se ele é primo: "))

if num % 1 == 0 and num % num == 0 and num % 2 != 0 and num % 3 != 0 and num % 5 != 0:
    print(f"{num} é um número primo!")
else:
    print(f"{num} não é um número primo!")
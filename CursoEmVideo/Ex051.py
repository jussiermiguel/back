"""
leia um número
diga se ele é primo ou não
"""

"""num = int(input("Digite um número para saber se ele é primo: "))

if num % 1 == 0 and num % num == 0 and num % 2 != 0 and num % 3 != 0 and num % 5 != 0:
    print(f"{num} é um número primo!")
else:
    print(f"{num} não é um número primo!")"""

# aqui é o código de guanabara
num = int(input("Digite um número: "))
tot = 0
for i in range (1, num+1):
    if num % i == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(f"{i}", end=' ')
print(f'\nO número {num} foi divisível {tot} vezes')
if tot == 2:
    print('E por isso ele é primo!')
else:
    print('E por isso ele não é primo')


"""
programa que leia um número e mostre o seu fatorial
"""
"""from math import factorial
n = int(input("Digite um número: "))
f = factorial(n)
print(f)"""
i = int(input("Digite um número para calcular o seu fatorial: "))
f = 1
#i = num
print(f"{i}! = ", end='')
while i > 0:
    print(f"{i}", end='')
    if i > 1:
        print(" x ", end='')
    else:
        print(' = ', end='')
    f *= i
    i -= 1
print(f"{f}")
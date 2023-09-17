"""
um programa que leia um numero e diga se ele é par ou impar
"""

num = int(input("Digite um número: "))

if num % 2 == 0:
    print(f"{num} é par!")
else:
    print(f"{num} é ímpar!")
"""
programa que leia o primeiro termo e a razão de uma PA
no final, mostre os 10 primeiros termos dessa progressão
"""
primeiro = int(input("Digite o primeiro termo da PA: "))
r = int(input("Informe a razão dessa PA: "))

for i in range(primeiro, primeiro + 10 * r, r):
    print(f"{i}", end= " -> ")


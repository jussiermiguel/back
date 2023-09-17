"""
programa que leia seis números inteiros
mostre a soma apenas dos pares
se for ímpar, desconsidere
"""
soma_pares = 0
for i in range(0, 6):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    if num % 2 == 0:
        soma_pares = soma_pares + num
print(f"A soma dos números pares digitados é: {soma_pares}")
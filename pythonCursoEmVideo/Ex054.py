"""
faça um programa que leia o peso de 5 pessoas
no final mostre qual foi o maior e o menor peso lidos
"""
"""pesos = []
for i in range (0, 5):
    peso = float(input(f"Digite o peso da {i+1}ª pessoa: "))
    pesos.append(peso)

pesos.sort()

print(f"O maior peso digitado foi {pesos[-1]}")
print(f"O menor peso digitado foi {pesos[0]}")"""

# guanabara
maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input(f"Peso da {i}ª pessoa: "))

    if i == 1:
        maior = peso
        menor = peso

    else:
        if i > maior:
            maior = peso
        if i < menor:
            menor = peso
print(f"O maior peso lido foi de {maior}kg")
print(f"O menor peso lido foi de {menor}kg")
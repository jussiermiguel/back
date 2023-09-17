"""
faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3
no intervalo de 1 até 500
"""
soma = 0
for i in range(1, 501, 2):
    if i % 3 == 0:  # posso usar qualquer um dos IFs
    #if i % 2 != 0 and not(i%3):
        print(i)
        soma += i
print(f"Essa é a soma dos números ímpares e múltiplos de 3: {soma}")

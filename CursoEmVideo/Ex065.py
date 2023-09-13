"""
crie um programa que leia vários numeros
no final mostre a media entre todos os valores
qual foi o maior e o menor
o programa deve perguntar se ele quer ou não continuar a digitar valores
"""
opcao = 'S'
cont = maior = menor = soma = 0
while opcao == 'S':
    num = int(input("Digite um número: "))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num < menor:
            menor = num
        else:
            menor = menor
        if num > maior:
            maior = num
        else:
            maior = maior
    opcao = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]

print("$"*30)
print(f"A quantidade de números digitados foi: {cont}")
print(f"A média dos números digitados é: {soma/cont}")
print(f"O maior número digitado foi: {maior}")
print(f"O menor número digitado foi: {menor}")
print("FIM")
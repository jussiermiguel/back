"""
crie um programa que leia vários numeros
o programa só vai parar quando o usuário digitar o valor 999
que é a condição de parada
no final mostre quantos numeros foram digitados e qual foi a soma entre eles
"""
num = cont = soma = 0
while num != 999:
    num = int(input("Digite um número[999 para parar]: "))
    if num != 999:
        soma = soma + num
        cont += 1

    else:
        soma = soma
        cont = cont
print(f"Foram digitados {cont} números")
print(f"A soma dos números é igual a: {soma}")
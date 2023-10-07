"""
faça um programa que mostre a tabuada de vários números
um de casa vez para cada valor digitado pelo usuário
o programa será interrompido quando um número negativo for digitado
"""

while True:
    print("*=*=*"*4 + "TABUADA DE MULTIPLICAÇÃO" + "*=*=*"*4)
    print("Zero para parar")
    num = int(input("Digite um número: "))
    if num == 0:
        break

    for i in range(1, 11):
        mult = num * i
        print(f"{num} * {i} = {mult}")
    """i = 0
    while i <= 10:
        mult = num * i
        print(f"{num} * {i} = {mult}")
        i+=1"""
print("*=*=*"*4 + "Finalizando a tabuada" + "*=*=*"*4)
print("ACABOU A TABUADA")
'''
programa que leia dois num int
compare-os
mostrando na tela o maior, menor ou igual
'''

i = 1
num = []
while i <= 2:
    num.append(input(f"Digite o {i}º numero: "))
    i+=1

if num[0] < num[1]:
    print(f"O número {num[1]} é maior que o número {num[0]}!")
elif num[1] < num[0]:
    print(f"O número {num[0]} é maior que o número {num[1]}!")
else:
    print(f"Os números {num[0]} e {num[1]} são iguais")
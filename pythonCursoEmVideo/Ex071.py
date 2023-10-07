"""
programa que simule o funcionamento de um caixa eletrônico
no início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.

OBS: considere que o caixa possui cédulas de 50, 20, 10 e 1
"""
print('='* 30)
print("{:^30}".format("BANCO"))
print('='* 30)
valor = int(input("Digite o valor que você quer sacar: R$ "))
total = valor
ced = 50
i = 0

while True:
    if total >= ced:
        total -= ced
        i += 1
    else:
        if i > 0:
            print(f"O total de {i} de cédulas de R$ {ced}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        i = 0
        if total == 0:
            break
print('=' * 15 + "Volte sempre" + '='* 15)
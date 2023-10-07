"""
faça um programa que jogue par ou ímpar com o computador
o jogo será interrompido quando o jogador perder
mostrando ao final o todal de vitórias do jogador no final do jogo
import random
print("Bem-vindo ao jogo Par ou Ímpar!")
vitorias = derrota = 0
while True:

    escolha = str(input("Escolha par (P) ou ímpar (I): ")).upper().strip()[0]
    if escolha == 'P':
        escolha = 'Par'
    elif escolha == 'I':
        escolha = 'Ímpar'
    else:
        print("Escolha inválida. Tente novamente.")
        continue

    num = int(input("Digite um número entre 0 e 10: "))
    if 0 <= num <= 10:
        num_comp = random.randint(0, 10)

        print(f"Você escolheu {num} e o computador escolheu {num_comp}")

        if escolha == 'Par':
            if (num + num_comp) % 2 == 0:
                print("Deu par")
                print('Parabéns, você ganhou!')
                vitorias += 1
            elif (num + num_comp) % 2 == 1:
                print("Deu ímpar")
                print('Você perdeu')
                derrota += 1
                break
        elif escolha == 'I':
            if (num + num_comp) % 2 == 1:
                print("Deu ímpar")
                print('Parabéns, você ganhou!')
                vitorias += 1
            elif (num + num_comp) % 2 == 0:
                print("Deu par")
                print('Você perdeu')
                derrota += 1
                break
    else:
        print('Número inválido')
        continue

print(f"Você teve um total de {vitorias} vitorias!")
"""
import random

print("Bem-vindo ao jogo Par ou Ímpar!")
vitorias = 0
while True:

    escolha = str(input("Escolha par (P) ou ímpar (I): ")).upper().strip()[0]
    if escolha not in ("P", "I"):
        print("Escolha inválida. Tente novamente.")
        continue

    num = int(input("Digite um número entre 0 e 10: "))
    if 0 <= num <= 10:
        num_comp = random.randint(0, 10)

        print(f"Você escolheu {num} e o computador escolheu {num_comp}")

        if escolha == "P":
            if (num + num_comp) % 2 == 0:
                print("Deu par")
                print('Parabéns, você ganhou!')
                vitorias += 1
            else:
                print("Deu ímpar")
                print('Você perdeu')
                break
        elif escolha == "I":
            if (num + num_comp) % 2 == 1:
                print("Deu ímpar")
                print('Parabéns, você ganhou!')
                vitorias += 1
            else:
                print("Deu par")
                print('Você perdeu')
                break
    else:
        print('Número inválido')
        continue

print(f"Você teve um total de {vitorias} vitorias!")
'''
crie um programa que faça o computador jogar jokenpô com você
'''
import random
jogo = ['Pedra', 'Papel', 'Tesoura']
usuario = input("Digite se você quer Pedra, Papel ou Tesoura: ").capitalize()
computador = random.choice(jogo)

print("*"*80)
print("-*-"*12, "->JO<-", "-*-"*12)
print("-\*-"*12, "->KEN<-", "-*-"*12)
print("-*-"*12, "->PÔ<-", "-*-"*12)
print("*"*80)

if computador == usuario:
    print(f"Computador -> {computador} x {usuario} <- Usuário")
    print("Empate")
else:
    if computador == "Pedra" and usuario == "Tesoura":
        print(f"Computador -> {computador} x {usuario} <- Usuário")
        print("Vitória minha")
    elif computador == "Pedra" and usuario == "Papel":
        print(f"Computador -> {computador} x {usuario} <- Usuário")
        print("Você me venceu")
    elif computador == "Papel" and usuario == "Tesoura":
        print(f"Computador -> {computador} x {usuario} <- Usuário")
        print("Você me venceu")
    elif computador == "Papel" and usuario == "Pedra":
        print(f"Computador -> {computador} x {usuario} <- Usuário")
        print("Te venci")
    elif computador == "Tesoura" and usuario == "Pedra":
        print(f"Computador -> {computador} x {usuario} <- Usuário")
        print("Perdi")
    elif computador == "Tesoura" and usuario == "Papel":
        print(f"Computador -> {computador} x {usuario} <- Usuário")
        print("Ganhei de você")
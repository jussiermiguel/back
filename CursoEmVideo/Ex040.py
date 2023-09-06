'''
a confederação nacional de natação precisa de um programa
leia o ano de nascimento e mostre sua categoria
até 9 infantil
até 14 junior
até 20 sub-20
até 40 profissional
acima master
'''
import datetime
ano_nascimento = int(input("Digite o ano de seu nascimento: "))
ano_atual = datetime.date.today().year

if ano_atual - ano_nascimento > 40:
    print(f"Você nasceu em {ano_nascimento}")
    print("Você é da categoria master!")
elif ano_atual - ano_nascimento > 20 and ano_atual - ano_nascimento <= 40:
    print(f"Você nasceu em {ano_nascimento}")
    print("Você é da categoria profissional")
elif ano_atual - ano_nascimento <= 20 and ano_atual - ano_nascimento > 14:
    print(f"Você nasceu em {ano_nascimento}")
    print("Você é da categoria sub-20")
elif ano_atual - ano_nascimento <= 14 and ano_atual - ano_nascimento > 9:
    print(f"Você nasceu em {ano_nascimento}")
    print("Você é da categoria Junior")
elif ano_atual - ano_nascimento <=9 and ano_atual - ano_nascimento > 0:
    print(f"Você nasceu em {ano_nascimento}")
    print("Você é da categoria infantil")
else:
    print("erro")
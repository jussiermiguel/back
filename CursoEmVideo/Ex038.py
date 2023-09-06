'''
leia o ano de nascimento
se ele ainda vai se alistar
se é hora de se alistar
se já passou do tempo

programa deve mostrar o tempo que falta ou que passou do prazo
'''
import datetime
print("*"*20, "Alistamento Militar", "*"*20)
ano_nascimento = int(input("Digite o ano de seu nascimento: "))
ano_atual = datetime.date.today().year

if ano_atual - ano_nascimento < 18:
    print(f"Você nasceu em {ano_nascimento}")
    print(f"Estamos em {ano_atual}")
    print(f"Ainda é cedo para o alistamento. Você só tem {ano_atual - ano_nascimento} anos")
    print(f"Ainda falta(am) {18-(ano_atual-ano_nascimento)} para o alistamento")
elif ano_atual - ano_nascimento > 18:
    print(f"Você nasceu em {ano_nascimento}")
    print(f"Estamos em {ano_atual}")
    print(f"Você está atrasado para o alistamento. Você já tem {ano_atual - ano_nascimento} anos")
    print(f"Você está com {ano_atual-(ano_nascimento+18)} ano(os) de atraso")
else:
#if ano_atual - ano_nascimento == 18:
    print(f"Você nasceu em {ano_nascimento}")
    print(f"Estamos em {ano_atual}")
    print(f"Está na hora do alismento. Você já está no ano em que completa {ano_atual-ano_nascimento} anos")

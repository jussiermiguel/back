"""
programa que diga se o ano é bissexto

"""
import datetime # importando a funcao de data

ano = int(input("Que ano quer analisar? Digite 0 para ver o ano atual: "))
if ano == 0:
    ano = datetime.date.today().year # pegando a data atual do computador
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0:
    print(f"{ano} é bissexto")
else:
    print(f"{ano} não é bissexto")

"""
programa que ler 7 anos
no final mostre quantos já atingiram a maioridade e quantos não atingiram
"""
import datetime
maior = 0
menor = 0
ano = datetime.date.today().year

for i in range (1, 8):
    nascimento = int(input(f"Qual o ano de nascimento da {i}ª: "))

    if ano - nascimento >= 18:
        maior += 1

    else:
        menor += 1

print(f"A quantidade de pessoas menores de idade é: {menor}")
print(f"A quantidade de pessoas de maior é: {maior}")

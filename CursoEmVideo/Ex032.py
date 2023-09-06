"""
faça um programa que leia 3 numeros e diga qual é o maior e qual é o menor
"""
lista_num = []
i = 1
while i <= 3:
    num = int(input(f"{i}º valor: "))
    lista_num.append(num)
    i+=1
    lista_num.sort()
print(lista_num)
print(f"o maior número digitado foi {lista_num[-1]}")
print(f"o menor número digitado foi {lista_num[0]}")

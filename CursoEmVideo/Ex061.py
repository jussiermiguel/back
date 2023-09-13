"""
refaça o desafio 050
lendo o primeiro termo e a razão de uma PA
mostrando os 10 primeiros termos usando while
"""
print("Gerador de PA")
primeiro = int(input("Primeiro termo: "))
r = int(input("Razão dessa PA: "))
i = 1
termo = primeiro
while i <= 10:
    print(f"{termo}", end=" -> ")
    termo += r
    i += 1
print("FIM")
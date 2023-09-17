"""
melhore o 61
perguntando se ele quer mostrar mais alguns termos
o programa encerra quando ele disser que quer mostrar 0 termos
"""

print("Gerador de PA")
primeiro = int(input("Primeiro termo: "))
r = int(input("Razão dessa PA: "))
i = 1
termo = primeiro
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while i <= total:
        print(f"{termo}", end=" -> ")
        termo += r
        i += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer mostrar a mais? "))
print(f"FIM! {total} termos")

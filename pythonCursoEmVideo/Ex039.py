'''
leia duas notas e calcule a media
mostrando no final media < 5 reprovado, media >= 5 e media < 7 recuperação, media >= 7 aprovado
'''
notas = 0
for i in range(1, 3):
    num = float(input(f"Digite a nota {i}: "))
    notas = notas + num

media = notas / i
if media >= 7:
    print(f"Média: {media}. Aprovado!")
elif media < 7 and media >= 5:
    print(f"Média: {media}. Recuperação!")
elif media < 5 and media >= 0:
    print(f"Média: {media}. Reprovado!")
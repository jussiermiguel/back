"""
programa que leia o NOME, IDADE e SEXO de 4 PESSOAS
no final mostre
a media de idade
qual o nome do homem mais velho
e quantas mulheres tem menos de 21 anos
"""

"""idades = 0
i_homens = 0
f_maior = 0
lista = [[], [], [], []]
for i in range (0, 4):
    nome = input("Digite o seu nome: ")
    idade = int(input("Digite a sua idade: "))
    print("Informe o seu sexo! ")
    sexo = input("M ou F: ").upper()
    pessoa = [nome, idade, sexo]
    lista.append(pessoa)

    idades += idade
    if sexo == 'F':
        if idade >= 21:
            f_maior += 1
    elif sexo == 'M':
        if idade > i_homens:
            homem_velho = nome
            velho = homem_velho
        elif i_homens == idade:
            velho = homem_velho + ' e ' + nome + 'são os mais velhos!'

print(lista)
print(f"A média de idade: {idades/len(lista)}")
print(f"O homem mais velho: {velho}")
print(f"Quantas mulheres tem menos de 21 anos: {f_maior}")"""
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
mulhernova = 0
for i in range(1, 5):
    print(f'----- {i}ª PESSOA -----')
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()

    somaidade += idade

    if i == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

    if sexo in 'Ff' and idade < 21:
        mulhernova += 1

mediaidade = somaidade / 4
print(f"A média de idade do grupo é de {mediaidade} anos.")
print(f"O homem mais velho tem {maioridadehomem} e se chama {nomevelho}.")
print(f"Ao todo são {mulhernova} com menos de 21 nos.")


"""
programa que leia o sexo de uma pessoa
mas só aceite M ou F
caso esteja errado, peça a digitação novamente até um valor correto
"""
sexo = str(input("Digite o seu sexo: [M/F]")).upper()[0].strip()

while sexo != 'M' and sexo != 'F':
    print("Dado inválido!")
    sexo = str(input("Digite o seu sexo: [M/F]")).upper().strip()

print("Sexo cadastrado com sucesso!")

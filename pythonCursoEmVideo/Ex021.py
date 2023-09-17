# programa que receba o nome completo de uma pessoa
nome_completo = str(input("Digite o seu nome: ")).strip()
print(len(nome_completo))

# exiba o nome com todas as letras Maiúsculas e Minúsculas
print(nome_completo.upper())
print(nome_completo.lower())

# conte quantas letras tem ao todo sem contar com os espaços
print(len(nome_completo)-nome_completo.count(' '))

# dizer quantas letras tem no primeiro nome
print(len(nome_completo.split()[0]))



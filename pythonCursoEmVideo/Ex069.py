"""
programa que leia a idade e sexo de varias pessoas
fazer com que o programa só aceite M ou F para sexo
a cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar
no final mostre
1) quantas pessoas tem mais de 18 anos
2) quantos homens foram cadastrados
3) quantas mulheres tem menos de 20 anos
"""
pessoasmais18 = homens = mulheresmenos20 = 0
while True:
    print("*"*50 + "Cadastro de pessoas" + "*"*50)
    idade = int(input("Idade: "))
    sexo = ' '
    while sexo not in "MF":
        sexo = str(input("Sexo [M/F]: ")).upper().strip()[0]

    if idade > 18:
        pessoasmais18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheresmenos20 += 1

    escolha = ' '
    while escolha not in "NS":
        escolha = str(input("Quer continuar? [S/N]")).upper().strip()[0]

    if escolha == 'N':
        break

print(f"A quantidade de pessoa que tem mais de 18 anos é: {pessoasmais18}")
print(f"A quantidade de homens é: {homens}")
print(f"A quantidade de mulheres que tem menos de 20 anos é: {mulheresmenos20}")
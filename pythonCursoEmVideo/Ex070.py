"""
programa que leia o nome e preco de vario produtos
o programa deverá perguntar se o usuário vai continuar
só pode aceitar S ou N
no final mostre:
1) qual é o total gasto na compra
2) quantos produtos custam mais de R$ 100
3) qual é o nome do produto mais barato
"""
preco_total = preco_mais_barato = preco_mais_caro = quant_mais_100 = i = 0

nome_mais_barato = ''
print("$" * 40 + "*****LOJA*****" + "$" * 40)
while True:
    print("*-"*15 + ">Produto<" + "-*"*15)
    nome = str(input("Digite o nome do produto: "))
    preco = float(input("Digite o valor do produto: R$ "))
    i += 1
    preco_total += preco

    if preco > 100:
        quant_mais_100 += 1

    if i == 1 or preco < preco_mais_barato:
        preco_mais_barato = preco
        nome_mais_barato = nome
        preco_mais_caro = preco

    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if escolha == 'N':
        break

print("-"*15 + "FIM DO PROGRAMA" + "-"*15)
print(f"O total da compra foi R$ {preco_total:.2f}")
print(f"Tempo {quant_mais_100} custando mais que R$ 100")
print(f"O produto mais barato foi {nome_mais_barato} e custou {preco_mais_barato:.2f}")

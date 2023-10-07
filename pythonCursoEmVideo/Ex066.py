"""
programa que leia vários números inteiros
o programa só para quando digitar 0
no final mostre quantos números foram digitados
e a soma entre eles, desconsiderando o 0
"""
quant = num = soma = 0

"""num = 1
while num != 0:
    num = 0"""
while True:
    print("<" + "="*50 + ">")
    print("SE QUISER PARAR, DIGITE [0]")
    num = int(input("Digite um número: "))

    """if num != 0:
        soma += num
        quant += 1"""
    """if num == 0:
        break

    soma+=num
    quant+=1"""

    if num == 0:
        break
    else:
        soma+=num
        quant+=1

print("<" + "="*50 + ">")
print(f"A soma entre os números é: {soma}")
print(f"A quantidade de números digitados foi: {quant}")
print("Fim do programa!")
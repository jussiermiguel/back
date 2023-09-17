'''
programa que calcule o valor a ser pago por um produto
considerando preço normal e condição de pagamento

à vista dinheiro/pix 10% de desconto
à vista cartão 5% de desconto
em até 2x no cartão preço normal
3x ou mais no cartão 20% de juros
'''
valor = float(input("Digite o valor do produto: "))

print(f"1- À vista dinheiro 10% de desconto R$ {valor - valor * 0.1:.2f}")
print(f"2- À vista cartão 5% de desconto R$ {valor - valor * 0.05:.2f}")
print(f"3- Até 2x preço normal R$ {valor:.2f}")
print(f"4- 3x ou mais no cartão 20% de juros R$ {valor + valor * 0.2}")

opcao = int(input("Escolha a forma de pagamento: "))

if opcao == 1:
    print(f"R$ {valor - valor * 0.1:.2f}")
    print("Compra Finalizada!")
elif opcao == 2:
    print(f"R$ {valor - valor * 0.05:.2f}")
    print("Compra Finalizada!")
elif opcao == 3:
    print(f"R$ {valor:.2f}")
    print("Compra Finalizada!")
elif opcao == 4:
    parcelas = int(input("Quantas parcelas? "))
    print(f"R$ {valor + valor * 0.2} em {parcelas}x")
    print(f"Parcelas de R$ {(valor + valor * 0.2)/parcelas}")
    print("Compra Finalizada!")
else:
    print("Erro")
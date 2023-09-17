'''
condições aninhadas

programa para aprovar o emprestimo bancario para compra de uma casa
o programa pergunta o VALOR DA CASA, o SALARIO de quem vai comprar e em QUANTOS ANOS ele vai pagar

calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o emprestimo será negado
'''

valor_casa = float(input("Digite o valor da casa: "))
salario = float(input("Informe o seu salário: "))
anos = int(input("Diga em quantos anos você quer financiar: "))

prestacao = valor_casa / (anos * 12)

if prestacao > salario * (30/100):
    print(f"Seu salário é R$ {salario:.2f}")
    print(f"A prestação de R$ {prestacao:.2f} é maior do que 30%(R$ {salario * (30/100)}) do seu salário")
    print("Empréstimo negado!")
else:
    print(f"Caso no valor de R$ {valor_casa:.2f}")
    print(f"Salário de R$ {salario:.2f}")
    print(f"Financiado em {anos} anos ou {anos*12} meses")
    print(f"Com prestações de R$ {prestacao:.2f}")

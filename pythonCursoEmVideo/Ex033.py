"""
programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
para salários superiores a 1.250 > aumento de 10%
para salários inferiores > aumento de 15%
"""

# recebendo o salário do funcionário
salario = float(input("Qual é o salário do funcionário? R$ "))

if salario <= 1250:  # quem recebe menos que 1250 receberá aumento de 15%
    print(f"R$ {salario:.2f} + aumento de 15% R$ {salario * 0.15:.2f}")
    print(f"Novo salário do funcionário é de R$ {salario * 1.15:.2f}")
else:  # quem tiver salário superior a 1250 receberá aumento de 10%
    print(f"R$ {salario:.2f} + aumento de 10% R$ {salario * 0.1:.2f}")
    print(f"Novo salário do funcionário é de R$ {salario * 1.1:.2f}")

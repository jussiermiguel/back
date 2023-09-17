salario = float(input("Qual é o seu salário? R$"))
aumento = salario * 0.15
salario_novo = salario + aumento
print("O seu salário atual é de R${:.2f}, com 15% (R${:.2f}) de aumento, vai passar a ser de R${:.2f}".format(salario,aumento,salario_novo))

"""
escreva um programa que leia a velocide de um carro
se ultrapassar 80KM/h mostre uma mensagem dizendo que ele foi multado
a multa vai custar 7 reais por cada KM acima do limite
"""
print("-+-"*20)
velocidade = float(input("Qual a velocidade que o carro passou no radar? "))#leitura da velocidade do carro
print("-+-"*20)

print("Velocidade permitida é 80km")
if velocidade > 80:
    print("Você foi multado!")
    print("Valor: R${:.2f}".format((velocidade-80)*7))
else:
    print('Tenha um bom dia, dirija com segurança!')

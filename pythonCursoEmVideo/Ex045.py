"""
faça um programa que mostre a contagem regressiva para o estouro de fogos de artifício
indo de 10 até 0
com uma pausa de 1s entre eles
"""
from time import sleep
print("Contagem para a virada do ano!")
for i in range(10, -1, -1):
    print(i)
    sleep(1)
print("BUM")

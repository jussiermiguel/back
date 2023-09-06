# crie um programa que leia um número real qualquer pelo teclado e mostre na tela a parte inteira desse número
num = float(input("Digite um número: "))

print('O valor digitado foi {} e sua parte inteira é {}'.format(num, num.__int__()))

'''num = float(input("Digite um número: "))

print('O valor digitado foi {} e sua parte inteira é {}'.format(num, int(num)))'''

'''from math import trunc
num = float(input("Digite um número: "))

print('O valor digitado foi {} e sua parte inteira é {}'.format(num, trunc(num)))'''

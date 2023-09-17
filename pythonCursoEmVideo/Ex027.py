"""
escreva um programa que faça o computador pensar em um numero inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador
o programa deve escrever na tela se o usuário ganhou ou perdeu o desafio
"""

from random import randint
print('O computador irá sortear um número entre 0 e 5.')
num_pc = randint(0,5)# um numero aleatório entre 0 e 5
num_usuario = int(input("Tente acertar o número: "))

if num_pc == num_usuario:
    print("Parabéns, você acertou!")# se o número sorteado e o número escolhido pelo usuário são iguais
else:
    print("Infelizmente você errou")# se os números não forem iguais

print("Aqui o resultado")
print("Número sorteado pelo computador: {}".format(num_pc))
print("Número que você informou: {}".format(num_usuario))

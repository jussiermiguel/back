"""
melhore o EX028 onde o computador vai pensar um numero entre 0 e 10
só que agora o jogador vai tentar adivinhar até acertar
mostrando no final quantos palpites foram necessários para vencer
"""

from random import randint
print('O computador irá sortear um número entre 0 e 10.')
num_pc = randint(0,10)# um numero aleatório entre 0 e 10
num_usuario = int(input("Tente acertar o número: "))
contador = 0
while num_pc != num_usuario:
    print("Infelizmente você errou! Tente novamente!")
    print('O computador irá sortear um número entre 0 e 10.')
    num_pc = randint(0, 10)  # um numero aleatório entre 0 e 10
    num_usuario = int(input("Tente acertar o número: "))
    contador += 1

print("Parabéns, você acertou!")# se o número sorteado e o número escolhido pelo usuário são iguais
print(f"Você precisou de {contador} tentativa(as) para acertar.")
print("Número sorteado pelo computador: {}".format(num_pc))
print("Número que você informou: {}".format(num_usuario))

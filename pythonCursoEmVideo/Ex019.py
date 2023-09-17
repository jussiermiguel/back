# programa para sortear um aluno de uma lista
import random

n1 = str(input("Digite um nome: "))
n2 = str(input("Digite um nome: "))
n3 = str(input("Digite um nome: "))
n4 = str(input("Digite um nome: "))
lista = [n1, n2, n3, n4]
escolhido = random.choices(lista, k=1)

print("Aluno escolhido: ", escolhido)


'''import random

n1 = str(input("Digite um nome: "))
n2 = str(input("Digite um nome: "))
n3 = str(input("Digite um nome: "))
n4 = str(input("Digite um nome: "))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)

print("Aluno escolhido: ", escolhido)'''
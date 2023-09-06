frase = str(input('Digite uma frase: ')).lower().strip()
print("A letra A foi digitada {} ".format(frase.count('a')))
print("A primeira vez que a letra A apareceu foi {}".format(frase.find('a')+1))# procurou a letra A da esquerda para a direita
print("A ultima vez que a letra A apareceu foi {}".format(frase.rfind('a')+1))# procurou da esquerda pra direita

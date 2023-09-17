"""
programa que leia um n inteiro
mostre na tela os n primeiros elementos de uma sequência de Fibonacci
"""
print("-+==+-"*10)
print("Sequência de Fibonacci")
print("-+==+-"*10)
n = int(input("Quantos termos você quer mostrar? "))
t1 = 0
t2 = 1
print("-+==+-"*10)
print(f"{t1} -> {t2}", end='')
i = 3
while i <= n:
    t3 = t1 + t2
    print(f" -> {t3}", end='')
    t1 = t2
    t2 = t3
    i += 1
print(" -> FIM")
print("-+==+-"*10)

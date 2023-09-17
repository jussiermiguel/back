'''
programa 34 (triangulo)
acrescentando o recurso de mostrar que tipo de triangulo será formado

equilátero todos lados iguais
isósceles dois lados iguais
escaleno todos lados diferentes
'''

print('<=' * 10, 'Analisando triângulo', '=>'*10)
r1 = float(input("Primeira reta: "))
r2 = float(input("Segunda reta: "))
r3 = float(input("Terceira reta: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("As retas podem formar um triângulo!", end='')
    if r1 == r2 == r3:
        print(f"{r1}, {r2}, {r3}. Todos iguais. Triângulo Equilátero")
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print(f"{r1}, {r2}, {r3}.Apenas um diferente. Triângulo Isósceles")
    else:
        print(f"{r1}, {r2}, {r3}.Todos diferentes. Triângulo Escaleno")
else:
    print("As retas não podem formar um triângulo!")
'''
leia o peso e altura
calcule imc
mostre seu status

< 18.5 abaixo do peso
e 25 peso ideal
e 30 sobrepeso
e 40 obesidade
> 40 obesidade mórbida
'''
#medidas = []

for i in range(0,2):
    if i == 0:
        altura = float(input("Digite a sua altura: "))
        #medidas.append(altura)
    else:
        peso = float(input("Digite o seu peso: "))
        #medidas.append(peso)
imc = peso/(altura*altura)

if imc < 18.5 and imc > 0:
    print(f"{imc:.2f}")
    print("Abaixo do peso!")
elif imc >= 18.5 and imc < 25:
    print(f"{imc:.2f}")
    print("Peso ideal!")
elif imc >= 25 and imc < 30:
    print(f"{imc:.2f}")
    print("Sobrepeso!")
elif imc >= 30 and imc < 40:
    print(f"{imc:.2f}")
    print("Obesidade!")
elif imc >= 40:
    print(f"{imc:.2f}")
    print("Obesidade Mórbida!")
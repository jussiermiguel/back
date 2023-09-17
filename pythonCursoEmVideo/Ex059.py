"""
crie um programa que leia dois valores e mostre um menu na tela
1 - somar
2 - multiplicar
3 - maior
4 - novos números
5 - sair

seu programa deverá realizar a operação solicitada em cada caso
"""
num1 = int(input("Primeiro valor: "))
num2 = int(input("Segundo valor: "))
opcao = 0
while opcao != 5:

    print('''Qual sua opção?
    1 - somar
    2 - multiplicar
    3 - maior
    4 - novos números
    5 - sair''')

    opcao = int(input(">"))

    if opcao == 1:
        print(f"{num1} + {num2} = {num1 + num2}")
    elif opcao == 2:
        print(f"{num1} * {num2} = {num1 * num2}")
    elif opcao == 3:
        if num1 > num2:
            print(f"{num1} é maior que {num2}")
        elif num2 > num1:
            print(f"{num2} é maior que {num1}")
        else:
            print(f"{num1} e {num2} são iguais")
    elif opcao == 4:
        print("Vamos recomeçar!")
        num1 = int(input("Primeiro valor: "))
        num2 = int(input("Segundo valor: "))
    elif opcao == 5:
        print("Estamos finalizando!")
    else:
        print("Opção inválida!")

print("FIM")
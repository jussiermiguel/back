"""
programa que pergunte a distância de uma viagem em KM
calcule o preço da passagem cobrando 0.50 por km para viagens de até 200km
e 0.45  para viagens mais longas
"""
distancia = float(input("Qual a distância (em km) da sua viagem? "))
# assim
preco = distancia * 0.5 if distancia <= 200 else distancia * 0.45
print(f"O preço da sua viagem será R$ {preco:.2f}")
# ou assim
'''if distancia <= 200:
    print(f"Você vai pagar {distancia*0.50:.2f} pela viagem de {distancia}km!")
else:
    print(f"Você vai pagar R$ {distancia*0.45:.2f} pela viagem de {distancia}km!")'''
print("Boa Viagem! ")
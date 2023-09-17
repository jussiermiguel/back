"""
crie um programa que leia uma frase e diga se ela é PALÍNDROMO
ARARA
APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA O BOLO
ANOTARAM A DATA DA MARATONA
"""
frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
   inverso += junto[letra]
print(f"O inverso de {junto} é {inverso}")
if inverso == junto:
    print("Temos um palíndromo!")
else:
    print("Não temos um palíndromo!")
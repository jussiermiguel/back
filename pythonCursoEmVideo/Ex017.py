# calculando catetos e hipotenusa
# recebe os catetos e retorna a hipotenusa

'''cat_oposto = float(input('Informe o valor do cateto oposto em cm: '))
cat_adjacente = float(input('Informe o valor do cateto adjacente em cm: '))

hipotenusa = (cat_oposto**2 + cat_adjacente**2) ** (1/2)
print('A hipotenusa é {:.2f}'.format(hipotenusa))'''

import math
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hi = math.hypot(co,ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))

'''from math import hypot
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hi = hypot(co,ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))'''

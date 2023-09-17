medida = float(input('Digite a distância (em metros) para ser convertida: '))
cm = medida * 100
mm = medida * 1000

print('A medida de {}m correspode a {:.0f}cm e {:.0f}mm'.format(medida, cm, mm))

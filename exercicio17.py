import math
adj = float(input('qual o valor do cateto adjacente?'))

opo = float(input('qual o valor do cateto oposto?'))

multi = (adj*adj) + (opo*opo)
print('essa vai ser a hipotenusa do triângulo: {}'.format(math.sqrt(multi)))
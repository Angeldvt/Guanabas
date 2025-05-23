r1 = int(input('digite um lado de um triângulo: '))
r2 = int(input('digite mais um lado de um triângulo: '))
r3 = int(input('digite mais um lado de um triângulo: '))

if r1 > r2 + r3 or r2 > r1 + r3 or r3 > r1 + r2:
    print('triângulo inválido!')
else:
    print('triângulo válido!')

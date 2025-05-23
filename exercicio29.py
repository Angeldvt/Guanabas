vel = float(input('Qual a velocidade o carro estava percorrendo? '))
multa = (vel - 80)*7

if vel > 80:
    print('você foi multado!')
    print(f'devera pagar {multa} reais')
else:
    print('você está dentro do limite de velocidade.')
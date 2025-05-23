preço = float(input('qual o preço do produto? '))
forma = int(input('qual a forma de pagamento?\n1 para á vista\n2 para á vista no cartão\n3 para 2x parcelado no cartão\n4 para 3x ou mais parcelado no cartão\n'))

vista = preço - (preço * 0.1)
cartaovista = preço - (preço * 0.05)
x3 = preço + (preço * 0.2)

if forma == 1:
    print(f'o preço vai ficar de {vista} reais')
elif forma == 2:
    print(f'o preço vai ficar de {cartaovista} reais')
elif forma == 3:
    print(f'o preço vai ser de {preço} reais')
elif forma == 4:
    print(f'o preço vai ser de {x3} reais')
else:
 print('forma de pagamento inválida.')

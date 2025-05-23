import random
n1 = int(input('Tente adivinhar um número entre 0 e 5 '))
lista = (0,1,2,3,4,5)
escolhido = random.choice(lista)
if escolhido == n1:
    print('Parabéns, você acertou!')
else:
    print('game over.')
print(f'o número escolhido foi {escolhido}')
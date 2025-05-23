ano = int(input('digite um ano qualquer: '))
bissexto = ano % 4
if bissexto == 0:
    print('é um ano bissexto! ')
else:
    print('é um ano comum. ')
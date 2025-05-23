num = int(input('digite um numero entre 0 e 9999'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'{u} é a unidade ')
print(f'{d} é a dezena')
print(f'{c} é a centena')
print(f'{m} é a milhar')
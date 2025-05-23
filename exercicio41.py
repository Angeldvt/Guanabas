nasci = int(input('digite o seu ano de nascimento: '))

idade = 2025 - nasci

if idade <= 9:
    print(f'nadador mirim, pois possui {idade} anos de idade')
elif idade <= 14 and idade > 9:
    print(f'nadador infantil, pois possui {idade} anos de idade')
elif idade <= 19 and idade > 14:
    print(f'nadador junior, pois possui {idade} anos de idade')
else:
    print(f'nadador senior, pois possui {idade} anos de idade.')
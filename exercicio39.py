nasci = int(input('digite seu ano de nascimento: '))

ano = 2025
idade = ano - nasci

if idade > 18:
    print(f'você já passou da idade de se alistar, está há {idade - 18} anos atrasado.')
elif idade < 18:
    print(f'você ainda deve se alistar, daqui {18 - idade} anos')
else:
    print('você está no ano de se alistar!')
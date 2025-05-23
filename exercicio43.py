altura = float(input('qual sua altura? '))
peso = float(input('qual seu peso?'))

imc = peso // (altura * altura)

if imc < 18.5:
    print(f'você está na faixa de abaixo do peso, com um imc de {imc}')
elif imc >= 18.5 and imc <= 25:
    print(f'você está na faixa de peso ideal, com um imc de {imc}')
elif imc > 25 and imc < 30:
    print(f'você está na faixa de acima do peso, com um imc de {imc} ')
elif imc > 30 and imc < 40:
    print(f'você está na faixa de obesidade, com imc de {imc}')
else:
    print(f'você está na faixa de obesidade mórbida, com um imc de {imc}')

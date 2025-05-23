n1 = int(input('digite sua primeira nota: '))
n2 = int(input('digite sua segunda nota: '))

média = (n1 + n2) / 2

if média < 5:
    print(f'você está reprovado, com média de {média}')
elif média > 5 and média < 7:
    print(f'você está de recuperação, com média de {média}')
else:
    print(f'aprovado, e sua média é de {média}')
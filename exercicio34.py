sal = int(input('digite seu salário para receber um aumento: '))
maior = sal/10 + sal
menor = (sal * 15 / 100) + sal

if sal <= 1250.00:
    print(f'seu salário foi para {menor} ')
else:
    print(f'seu salário foi para {maior}')
valorcasa = int(input('qual o valor da casa?'))
salario = int(input('qual o seu sálario?'))
anos = int(input('em quantos anos será pago?'))

mensal = valorcasa / (anos * 12)
porcen = salario * 0.3

if mensal > porcen:
    print('Sálario insuficiente')
else:
    print(f'vai sair por {mensal} reais por mês')
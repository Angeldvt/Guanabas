import random

Itens = (1,2,3)
computador = random.choice(Itens)

escolha = input('Escolha\n[1] para pedra\n[2] para papel\nescolha [3] para tesoura.')

if escolha == "1":
    if computador == 1:
        print('EMPATE!')
    elif computador == 2:
        print('VOCÊ PERDEU, O COMPUTADOR ESCOLHEU PEDRA')
    elif computador == 3:
        print('VOCÊ GANHOU, O COMPUTADOR ESCOLHEU TESOURA')
elif escolha == "2":
    if computador == 1:
        print('VOCÊ GANHOU, O COMPUTADOR ESCOLHEU PEDRA!')
    elif computador == 2:
        print('EMPATE!')
    elif computador == 3:
        print('VOCÊ PERDEU, O COMPUTADOR ESCOLHEU PAPEL')
elif escolha == "3":
    if computador == 1:
        print('VOCÊ PERDEU, O COMPUTADOR ESCOLHEU PEDRA')
    elif computador == 2:
        print('VOCÊ GANHOU, O COMPUTADOR ESCOLHEU PAPEL')
    elif computador == 3:
        print('EMPATE!')

import random
cr1 = str(input('digite o nome de um aluno: '))
cr2 = str(input('digite o nome de um aluno: '))
cr3 = str(input('digite o nome de um aluno: '))
cr4 = str(input('digite o nome de um aluno: '))
lista = (cr1 , cr2 , cr3 , cr4 )
escolhido = random.choice(lista)
print(f'esse foi o nome escolhido: {escolhido}')

dist = int(input('de quantos quilometros será sua viagem? '))
curtas = dist*0.5
longas = dist*0.45
if dist <= 200:
    print(f'o valor cobrado será {curtas}')
else:
    print(f'o valor cobrado será {longas}')
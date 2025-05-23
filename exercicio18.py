import math
num = float(input('digite o numero que queiras saber o angulo'))

cos =  math.cos(math.radians(num))
sen = math.sin(math.radians(num))
tan = math.tan(math.radians(num))

print('esse é o cosseno do angulo {} = {:.2f}'.format(num, cos))
print('esse é o seno do angulo {} = {:.2f}'.format(num, (sen)))
print('essa é a tangente do angulo {} = {:.2f}'.format(num, tan))
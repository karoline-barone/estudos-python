#leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo
from math import radians, sin, cos, tan
ang = float(input('Digite o valor do angulo: '))
seno = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print(f'O angulo de {ang} tem o seno de {seno:.2f}, cosseno de {cos:.2f}, tangente {tan:.2f}')



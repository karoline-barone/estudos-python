#leia o comprimento do cateto oposto e adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa
from math import hypot
catop = float(input('Digite o valor do cateto oposto: '))
catadj = float(input('Digite o valor do cateto adjacente: '))
print(f'A hipotenusa vai medir {hypot(catop, catadj):.2f}')



''' Solucao alternativa:
catop = float(input('Digite o comprimento do cateto oposto: '))
catadj = float(input('Digite o comprimento do cateto adjacente: '))
hip = (catop**2 + catadj**2) ** (1/2)
print(f'A hipotenusa vai medir {hip:.2f}')'''


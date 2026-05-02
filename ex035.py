#leia o comprimento de tres retas e diga ao usuário se elas podem ou nao formar um triangulo
r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possível formar um triangulo.')
else: print('Não é possível formar um triangulo.')
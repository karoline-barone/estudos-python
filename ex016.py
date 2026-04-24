#leia um número real e mostre na tela a sua porcao inteira
from math import trunc
num = float(input('Digite um numero real: '))
print(f'O valor digitado foi {num} e a sua porcao inteira é {trunc(num)}')

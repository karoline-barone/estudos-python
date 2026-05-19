#leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
num=int(input('Digite um número de 0 a 9999: '))
print(f'Unidade: {num % 10}')
print(f'Dezena: {num // 10 % 10}')
print(f'Centena: {num // 100 % 10}')
print(f'Milhar: {num // 1000 % 10}')
# escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de fibonacci
n = int(input('Quantos termos deseja mostrar: '))
termo = 1
soma = 1
primeiro = 0
proximo = 1
print('0 -> ', end='')
while n > termo:
    print(f'{soma} -> ', end='')
    soma = primeiro + proximo
    primeiro = proximo
    proximo = soma
    termo+=1
print('FIM')

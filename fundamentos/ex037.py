# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão, 1 para binário, 2 para octal, 3 para hexadecimal
num = int(input('Digite um número inteiro: '))
escolha = int(input('Escolha a base de conversão: \n 1 - binário \n 2 - octal \n 3 - hexadecimal \n'))
if escolha == 1:
    print(f'{num} convertido para binário é igual a {bin(num)[2:]}')
elif escolha == 2:
    print(f'{num} convertido para octal é igual a {oct(num)[2:]}')
elif escolha == 3:
    print(f'{num} convertido para hexadecimal é igual a {hex(num)[2:]}')
else:
    print('Opção inválida. Tente novamente.')
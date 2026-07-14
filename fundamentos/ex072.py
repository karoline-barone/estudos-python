'''Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito','dezenove', 'vinte')
escolha = int(input('Escolha um número entre 0 e 20: '))
while escolha < 0 or escolha > 20:
    escolha = int(input('Escolha um número entre 0 e 20: '))
print(f'Você escolheu o número {numeros[escolha]}.')

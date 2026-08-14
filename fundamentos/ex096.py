'''Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e
comprimento) e mostre a área do terreno.'''
def area(larg, comp):
    area = larg * comp
    print(f'O terreno possui {area}m².')


larg = float(input('Qual a largura do terreno?: '))
comp = float(input('Qual o comprimento do terreno?: '))
area(larg, comp)

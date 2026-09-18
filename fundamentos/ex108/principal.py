'''Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um
valor monetário formatado.'''
from ex108 import moeda

valor = float(input('Digite um valor: R$ '))
print(f'A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}')
print(f'O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}')
print(f'Aumentando 15% temos {moeda.moeda(moeda.aumentar(valor, 15))}')
print(f'Diminuindo 8% temos {moeda.moeda(moeda.diminuir(valor, 8))}')

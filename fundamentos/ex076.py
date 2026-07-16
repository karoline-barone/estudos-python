#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
produtos = ('Mouse', '49.90', 'Teclado', '120.00', 'Fone', '81.50', 'Notebook', '2500.00',
            'Monitor', '330.80', 'Tablet', '940.00')
print(f'{"LISTAGEM DE PRODUTOS".center(40, "-")}')
for i in range (0, len(produtos)):
    if i % 2 == 0:
        print(f'{produtos[i]:.<30}', end = '')
    else:
        print(f'R${produtos[i]:>7}')

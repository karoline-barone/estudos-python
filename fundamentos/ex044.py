''' Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preco normal e condicao de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preco normal
- 3x ou mais no cartão: 20% de juros'''
total = float(input('Qual o valor do produto? R$ '))
formapag = int(input('''Qual a forma de pagamento?
 [ 1 ] à vista dinheiro/cheque
 [ 2 ] à vista cartão
 [ 3 ] 2x no cartão
 [ 4 ] 3x ou mais no cartão \n'''))
if formapag == 1:
    print(f'Pagando à vista em dinheiro/cheque, você tem 10% de desconto, sua compra de R$ {total:.2f} vai custar R$ {total * 0.9:.2f}.')
elif formapag == 2:
    print(f'Pagando à vista no cartão, você tem 5% de desconto, sua compra de R$ {total:.2f} vai custar R$ {total * 0.95:.2f}.')
elif formapag == 3:
    print(f'Pagando em 2x no cartão, o valor se mantém. Sua compra será parcelada em 2x de {total/2:.2f}. Sua compra de R$ {total:.2f} vai custar R$ {total:.2f}.')
elif formapag == 4:
    parcelas = int(input('Quantas parcelas? '))
    print(f'Pagando em 3x ou mais no cartão, acrescenta 20% de juros. Sua compra será parcelada em {parcelas}x de {(total * 1.2)/parcelas:.2f}. Sua compra de R$ {total:.2f} vai custar R$ {total * 1.2:.2f}.')
else:
    print('Opcao invalida. Tente novamente.')

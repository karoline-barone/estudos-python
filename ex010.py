#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
#considere US$1.00 = R$ 3.27
reais = float(input('Digite a quantidade de reais: '))
print(f'Pode comprar {reais/3.27:.2f} dolares')
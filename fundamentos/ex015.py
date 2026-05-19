#pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado
#calcule o valor a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado
km = float(input('Quantos km rodados? '))
dias = int(input('Quantos dias alugados? '))
print(f'O valor a pagar é R${(km*0.15)+(dias*60):.2f}')
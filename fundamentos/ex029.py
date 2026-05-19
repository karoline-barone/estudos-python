#leia a velocidade de um carro, se ele ultrapassar 80km/h mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada km acima do limite
vel = int(input('Qual a velocidade do carro em km/h? '))
if vel > 80:
    print(f'Voce foi multado em R${(vel-80)*7:.2f}!')
else:
    print('Voce está dentro do limite de velocidade!')
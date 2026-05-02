# pergunte a distancia de uma viagem em km. Calcule o preco da passagem cobrando R$ 0,50 por km para viagens de até 200 km e R$ 0,45 para viagens mais longas
dist = float(input('Digite a distancia da viagem em km: '))
if dist <= 200: print(f'O preço da passagem é: R${(dist*0.50):.2f}')
else: print(f'O preço da passgem é: R${(dist*0.45):.2f}')
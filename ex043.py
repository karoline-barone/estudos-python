''' Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 - 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida'''
peso = float(input('Digite o seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / (altura ** 2)
print(f'Seu IMC é {imc:.1f}. \n')
if imc < 18.5: print('Você está abaixo do peso!')
elif imc >= 18.5 and imc < 25: print('Você está no peso ideal!')
elif imc >= 25 and imc < 30: print('Você está em sobrepeso!')
elif imc >= 30 and imc < 40: print ('Você está em obesidade!')
elif imc >= 40: print('Você está em obesidade mórbida!')

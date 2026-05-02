#leia tres numeros e mostre qual é o maior e qual é o menor
num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segundo numero: '))
num3 = float(input('Digite o terceiro numero: '))
#verificando maior
if num1 > num2 and num1 > num3:
    maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
#verificando menor
if num1 < num2 and num1 < num3:
    menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3

print(f'O maior número digitado foi {maior} e o menor foi {menor}.')
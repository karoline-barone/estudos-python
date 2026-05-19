#desenvolva um programa que leia o primeiro termo e a razao de uma PA. No final, mostre os 10 primeiros termos dessa progressao.
primeirotermo = int(input('Qual o primeiro termo? '))
razao = int(input('Qual a razão? '))
for c in range(primeirotermo, primeirotermo + razao*10, razao):
    print(c, end=' -> ')
print('FIM')
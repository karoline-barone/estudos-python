#leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta para pintá-la
#sabendo que cada litro de tinta pinta uma área de 2m²
larg = float(input('Qual a largura da parede em metros?'))
alt = float(input('Qual a altura da parede em metros?'))
area = larg*alt
print(f'A área da parede é {area} e a quantidade de tinta necessária é {area/2} litros')
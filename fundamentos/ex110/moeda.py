def aumentar(valor, taxa, formatar = False):
    resultado = valor + (valor * (taxa/100))
    return resultado if formatar == False else moeda(resultado)


def diminuir(valor, taxa, formatar = False):
    resultado = valor - (valor * (taxa/100))
    return resultado if formatar == False else moeda(resultado)


def dobro(valor, formatar = False):
    resultado = valor * 2
    return resultado if formatar == False else moeda(resultado)


def metade(valor, formatar = False):
    resultado = valor / 2
    return resultado if formatar == False else moeda(resultado)

def moeda(valor):
    return f'R${valor:.2f}'.replace('.', ',')

def resumo(valor, taxaaum, taxared):
    print('-' * 40)
    print(f'Resumo do valor: {moeda(valor)}'.center(40))
    print('-' * 40)
    print(f'Dobro do valor: \t\t{dobro(valor, True)}')
    print(f'Metade do valor: \t\t{metade(valor, True)}')
    print(f'{taxaaum}% de aumento: \t\t{aumentar(valor, taxaaum, True)}')
    print(f'{taxared}% de redução: \t\t{diminuir(valor, taxared, True)}')
    print('-' * 40)
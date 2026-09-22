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
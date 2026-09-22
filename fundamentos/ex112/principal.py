'''Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro()
que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas valores que seja monetários.'''
from ex112.utilidadescev import moeda
from ex112.utilidadescev import dado

valor = dado.leiaDinheiro('Digite um valor: R$ ')
moeda.resumo(valor, 15, 10)

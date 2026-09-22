def leiaDinheiro(msg):
    while True:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'Erro!"{entrada}" é um preço inválido.')
        else:
            return float(entrada)

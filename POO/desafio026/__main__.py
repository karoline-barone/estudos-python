'''Desafio026 - Crie a estrutura capaz de calcular salários de funcionários diferentes:
- Funcionario (abstract) = nome, sal_bruto, salario, sal_min = 1612, inss = 7.5, calc_sal() {abstract}, analisar_sal()
- Horista = valor_hora(), horas_trab(), calc_sal()
- Mensalista = calc_sal() '''
from funcionarios import *

def main():
    f1 = Horista("Ana", 45, 220)
    f1.calc_sal()
    f1.analisar_sal()

    f2 = Mensalista("Pedro", 5000)
    f2.calc_sal()
    f2.analisar_sal()

if __name__ == '__main__':
    main()
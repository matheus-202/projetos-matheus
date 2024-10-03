print('Este programa informa a comissão de um vendedor ')

nome = input('Insira o nome do vendedor: ')
sal = float(input('Insira o salário fixo do vendedor: '))
vendas = float(input('Insira o total de vendas no mês: '))
COMOSSISAO = 15
sal_total= 0

def comissao(vendas_mês,sal_mes,comis_ao):
    comi = sal_mes + ((vendas_mês*comis_ao)/15)
    return comi

sal_total = comissao(sal,vendas,COMOSSISAO)

print('Este mês o vendedor',nome,'recebeu R$',sal_total)

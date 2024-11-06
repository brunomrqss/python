dias_uteis = 26
valor_diaria = int(input())
qtd_faltas = int(input())

salario_integral = valor_diaria * dias_uteis
salario_com_desconto = 0
salario_bonificado = 0

bonificacao = ''

if qtd_faltas > 0:
    bonificacao = 'nao'
    salario_com_desconto = (dias_uteis - qtd_faltas) * valor_diaria

if qtd_faltas == 0:
    bonificacao = 'sim'
    salario_bonificado = salario_integral * 1.123

print(f'Salário integral: R${salario_integral}')
print(f'Quantidade de faltas: {qtd_faltas}')
print(f'Salário com desconto: R${salario_com_desconto}')
print(f'Elegível para bonificação? {bonificacao}')
print(f'Salário com bonificação: R${salario_bonificado}')
      
    


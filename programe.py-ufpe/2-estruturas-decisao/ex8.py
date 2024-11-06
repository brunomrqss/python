valor_diaria = int(input())
dias_trabalhados = int(input())

salario_bruto = valor_diaria * dias_trabalhados
salario_liquido = salario_bruto
imposto_renda = 0

if salario_bruto <= 1999:
    print(f'Salário bruto: R${salario_bruto}')
    print('Isento de Imposto de Renda')
    print(f'Salário líquido: R${salario_liquido:.0f}')
elif salario_bruto >= 2000 and salario_bruto <= 5000:
    print(f'Salário bruto: R${salario_bruto}')
    imposto_renda = 0.15
    print(f'Imposto de Renda (IR) 15%: R${salario_liquido * imposto_renda:.0f}')
    salario_liquido *= 0.85
    print(f'Salário líquido: R${salario_liquido:.0f}')
else:
    print(f'Salário bruto: R${salario_bruto}')
    imposto_renda = 0.275
    print(f'Imposto de Renda (IR) 27.5%: R${salario_liquido * imposto_renda:.0f}')
    salario_liquido *= 0.725
    print(f'Salário líquido: R${salario_liquido:.0f}')


    
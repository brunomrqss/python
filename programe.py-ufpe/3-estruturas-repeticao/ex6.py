folha_geral = 0
qtd_funcionarios = 0

for i in range(10):
    qtd_funcionarios+=1 
    salario = int(input(f'informe o salario do {i+1} funcionario: '))
    folha_geral += salario

media = folha_geral / qtd_funcionarios 

print(f'Valor total gasto com a folha salarial = {folha_geral}')
print(f'Média de salário geral dos funcionários = {media}')

funcionarios = []

for i in range(2):

    funcionario={}

    nome=input('informe o nome: ')
    salario=int(input('informe o salario: '))

    funcionario['nome']=nome
    funcionario['salario']=salario

    funcionarios.append(funcionario)

aumento=1.1
reducao=0.9

for i in range(len(funcionarios)):
    percentual=int(input(f'informe um percentual 1-aumento/2-redução para o(a) {funcionarios[i]['nome']}: '))

    if percentual==1:
        funcionarios[i]['salario']*=aumento
        print()
        print(f'Aumento salarial para o {funcionarios[i]['nome']} de 10%\nNovo salário é de R${funcionarios[i]['salario']:.2f}')
    else:
        funcionarios[i]['salario']*=reducao
        print()
        print(f'Redução salarial para o {funcionarios[i]['nome']} de 10%\nNovo salário é de R${funcionarios[i]['salario']:.2f}')

lista_funcionarios=[]

for rep in range(3):

    funcionario={}

    nome=input('informe o nome: ')
    cpf=input('informe o cpf: ')
    salario=int(input('informe o salario: '))

    funcionario["cpf"]=cpf
    funcionario["nome"]=nome
    funcionario["salario"]=salario

    lista_funcionarios.append(funcionario)

maior_salario=lista_funcionarios[0]["salario"]

for dict in lista_funcionarios:
    if dict["salario"]>maior_salario:
        maior_salario=dict["salario"]

for funcionario in lista_funcionarios:
    if funcionario["salario"]>=maior_salario:
        print(f'CPF do maior salário: {funcionario["cpf"]}')
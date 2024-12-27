def cadastro_funcionario():
    count=0

    funcionario={}
    funcionarios=[]

    while count!=1:
        nome=input('informe o nome: ')
        salario=int(input('informe o salario: '))
        cpf=input('informe o cpf: ')
        dp=input('informe o dp: ')

        funcionario['nome']=nome
        funcionario['salario']=salario
        funcionario['cpf']=cpf
        funcionario['dp']=dp

        funcionarios.append(funcionario)

        count=int(input('deseja encerrar o cadastro 1-sim/0-nao: '))

        if count==1:
            break
    
cadastro_funcionario()
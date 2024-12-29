def cadastro(nome, cpf, salario, dp):
    funcionario = {
        'cpf':cpf,
        'nome':nome,
        'salario': salario,
        'departamento': dp
    }

    funcionarios.append(funcionario)
    print('Funcionário cadastrado com sucesso!')

funcionarios=[]

while True:
    resposta=input('Deseja cadastrar um funcionario s-sim/n-nao? ')

    if resposta=='s'.lower():
        cpf=input('informe o cpf: ')
        nome=input('informe o nome do funcionario: ')
        salario=int(input('informe o salario do funcionario: '))
        departamento=input('informe o departamento: ')

        cadastro(nome, cpf, salario, departamento)
        print(f'Funcionarios cadastrados: \n{funcionarios}')
    else:
        break

def cpf_repetido(cpf):
    for funcionario in funcionarios:
        if funcionario['cpf']==cpf:
            print('funcionario já cadastrado')
    
    return False

cpf_repetido('11489524460')
funcionarios = []

# Coleta dados dos funcionários
count = 0
while count < 3:
    # Cria o dicionário
    funcionario = {}
    nome = input('Informe o nome: ')
    salario = int(input('Informe o salário: '))

    # Adiciona nome e salário ao dicionário
    funcionario['nome'] = nome
    funcionario['salario'] = salario

    # Adiciona o dicionário à lista de funcionários
    funcionarios.append(funcionario)
    count += 1

# Verifica repetição de salários
salarios_repetidos = {}
for funcionario in funcionarios:
    salario = funcionario['salario']
    nome = funcionario['nome']

    if salario in salarios_repetidos:
        salarios_repetidos[salario].append(nome)  # Adiciona o nome ao salário já existente
    else:
        salarios_repetidos[salario] = [nome]  # Cria a chave do salário com o nome

# Exibe os salários repetidos e os respectivos funcionários
for salario, nomes in salarios_repetidos.items():
    if len(nomes) > 1:  # Apenas salários com mais de um funcionário
        print(f"Salário {salario} é compartilhado pelos funcionários: {', '.join(nomes)}.")

sombra_predio = float(input('informe a sombra do prédio: '))
sombra_pessoa = float(input('informe a sombra da pessoa: '))
altura_pessoa = float(input('informe a altura da pessoa: '))

altura_predio = (sombra_predio/sombra_pessoa) * altura_pessoa

print(f'altura: {altura_predio}')

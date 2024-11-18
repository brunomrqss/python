stop = 0

contador_masc = 0
contador_fem = 0

soma_salario_masc = 0
soma_salario_fem = 0


while stop == 0:
    sexo = input('informe o genero do funcionario(a) m- masculino/f- feminino: ')
    if sexo == 'm':
        salario = int(input('informe o salario: '))
        soma_salario_masc += salario
        contador_masc +=1
    elif sexo == 'f':
        salario = int(input('informe o salario: '))
        soma_salario_fem += salario
        contador_fem += 1 
    else:
        sexo = input('genero invalido!')
        break

    encerrar = input('1-adicionar outro funcionario / 2- finalizar formulario: ')
    if encerrar == '2':
        break

media_salario_masc = soma_salario_masc/contador_masc
media_salario_fem = soma_salario_fem/contador_fem

print(f'A quantidade de funcionários do sexo masculino foi de {contador_masc} e a quantidade de funcionárias femininas foi de {contador_fem}')
print(f'O valor total pago para funcionarios(as) do sexo masculino e feminino respectivamente foi de R${soma_salario_masc} e R${soma_salario_fem}')
print(f'A média salarial dos funcionários(as) masculino e feminino respectivamente foram de R${media_salario_masc} e R${media_salario_fem}')

    
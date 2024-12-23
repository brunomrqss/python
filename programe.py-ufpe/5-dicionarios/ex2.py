funcionarios = {}

for i in range(3):
    nome=input('informe o nome: ')
    cpf=input('informe o cpf: ')

    funcionarios[cpf]={'nome':nome}

lista_funcionarios=[]

for cpf, dados in funcionarios.items():
    lista_funcionarios.append((cpf, dados["nome"]))

# ordenação

for i in range(len(lista_funcionarios)-1):
    menor=i
    for j in range(i+1, len(lista_funcionarios)):
        if lista_funcionarios[j][1] < lista_funcionarios[menor][1]:
            menor=j
        
    lista_funcionarios[i],lista_funcionarios[menor]=lista_funcionarios[menor], lista_funcionarios[i]


print('funcionarios por ordem')
print()

for cpf, nome in lista_funcionarios:
    print(f'cpf: {cpf}, nome: {nome}')
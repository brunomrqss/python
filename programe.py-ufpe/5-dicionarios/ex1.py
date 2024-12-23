# Faça um programa para ler cpf, nome, salário de 10 funcionários. Ao final da leitura, 
# exibir os nomes e salários de quem tem salário abaixo e acima da média, nessa ordem.

funcionarios=[]

for cont in range(3):
    funcionario = {}
    cpf=input('informe o cpf do funcionario: ')
    nome=input('informe o nome do funcionario: ')
    salario=float(input('informe o salario do funcionario: '))
   

    funcionario["nome"]=nome
    funcionario["salario"]=salario 
    funcionario["cpf"]=cpf

    funcionarios.append(funcionario)

soma_salario=0

for dic in funcionarios:
    soma_salario+=dic["salario"]

media_salarial=soma_salario/len(funcionarios)
print(f"\nA media salaria é de R${media_salarial:.2f}")

for dic in funcionarios:
    if dic["salario"]>media_salarial:
        print(f"\n{dic["nome"]} com salario de R${dic["salario"]} tem o salario acima da media")
    else:
        print(f"\n{dic["nome"]} com salario de R${dic["salario"]} tem o salario abaixo da media")


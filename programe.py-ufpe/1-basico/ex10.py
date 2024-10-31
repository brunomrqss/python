'''
Escreva um programa que leia o salário de uma pessoa, quantas horas ela trabalha por dia e quantos dias ela trabalhou no mês. 
Em seguida, calcule e exiba quanto essa pessoa recebe por hora.
'''

salario = int(input('salario: '))
horas_trabalhadas = int(input('horas trabalhadas: '))
dias_trabalhados = int(input("dias trabalhados: "))

valor_hora = (salario/horas_trabalhadas) / dias_trabalhados

print(f"Valor da hora trabalhada: R${valor_hora:.2f}")
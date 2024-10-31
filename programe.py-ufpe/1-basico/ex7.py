"""
Escreva um programa que, leia um valor de custo e o percentual de lucro desejado, e na sequencia mostre o valor final do produto;
"""
valor_custo = float(input("digite o valor do produto: "))
percentual = int(input("informe o percentual de lucro que voce deseja obter sobre o produto: "))/100
print(f"Lucro de {percentual*100:.0f}%")

diferenca = valor_custo * percentual 

valor_final = valor_custo + diferenca
print(f"Valor final do produto: R${valor_final:.2f}")
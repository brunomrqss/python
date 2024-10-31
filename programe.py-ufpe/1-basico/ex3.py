"""
Faça um programa que, solicite a altura e o raio de um cilindro, calcule o volume total do cilindro (use π=3.14) e exiba esse valor.
"""
altura = int(input("digite o valor da altura do cilindro: "))
raio = int(input("digite o valor do raio do cilindro: "))
pi = 3.14
volume = pi*(raio**2)*altura

print(f"O volume do cilindro é de {volume}")

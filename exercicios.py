# Entrada de X
X = float(input("Digite o valor de X: "))

# Variável para armazenar o resultado da soma
soma = 0

# Loop de 1 até 25
for i in range(1, 26):
    # Expoente da potência de X
    expoente = 26 - i
    
    # Calcula o termo da série
    termo = (X ** expoente) / i
    
    # Alterna entre soma e subtração
    if i % 2 == 1:
        soma += termo
    else:
        soma -= termo

# Exibe o resultado final
print(f"A soma da série é: {soma}")

# Inicializar a lista vazia
letras = []

# Receber 10 letras do usuário
print("Digite 10 letras:")
for i in range(10):
    letra = input(f"Letra {i+1}: ").strip().lower()  # Garantir que seja minúscula e sem espaços
    letras.append(letra)

# Calcular a quantidade de repetições de cada letra
letras_ja_verificadas = []  # Para evitar mostrar a contagem duplicada
repeticoes = []  # Lista para armazenar a contagem de cada letra

print("\nQuantidade de repetições de cada letra:")
for letra in letras:
    if letra not in letras_ja_verificadas:
        letras_ja_verificadas.append(letra)  # Marcar a letra como verificada
        quantidade = letras.count(letra)  # Contar ocorrências na lista
        repeticoes.append((letra, quantidade))  # Adicionar a letra e a contagem
        print(f"{letra}: {quantidade}")

# Encontrar maior e menor quantidade de repetições sem lambda
maior_repeticao = repeticoes[0]
menor_repeticao = repeticoes[0]

for letra, quantidade in repeticoes:
    if quantidade > maior_repeticao[1]:
        maior_repeticao = (letra, quantidade)
    if quantidade < menor_repeticao[1]:
        menor_repeticao = (letra, quantidade)

# Mostrar resultados
print(f"\nLetra com maior quantidade de repetições: {maior_repeticao[0]} ({maior_repeticao[1]} vezes)")
print(f"Letra com menor quantidade de repetições: {menor_repeticao[0]} ({menor_repeticao[1]} vez(es))")

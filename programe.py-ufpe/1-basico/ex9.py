lado = int(input("informe a medida do lado do terreno: "))
altura = int(input("informe a altura do terreno: "))

valor_metro_quadrado = 50

area_total_concretagem = lado * altura

valor_total_concretagem = area_total_concretagem * valor_metro_quadrado 

print(f"O valor total para concretagem total do terreno de {area_total_concretagem}m² é de R${valor_total_concretagem:.2f}")
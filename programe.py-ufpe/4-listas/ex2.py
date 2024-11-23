lista_letras = []

for i in range(10):
    letra = input(f"Informe a {i+1}ª letra: ")
    lista_letras.append(letra)

lista_letras.sort()
lista_letras.reverse()
print(lista_letras)
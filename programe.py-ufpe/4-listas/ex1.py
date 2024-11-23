lista_letras = []

for i in range(10):
    letra = input(f'Informe o a {i+1}º letra: ')

    lista_letras.append(letra)

lista_letras.reverse()
print(lista_letras)
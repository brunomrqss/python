lista_letras = []

for i in range(10):
    letra = input(f"Informe a {i+1}ª letra: ")
    lista_letras.append(letra)

for i in lista_letras:
    if lista_letras.count(i) > 1:
        lista_letras.remove(i)
    
print(lista_letras)
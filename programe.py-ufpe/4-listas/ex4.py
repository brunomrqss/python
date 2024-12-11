lista=[]

for i in range(10):
    letra=input('letra: ')
    lista.append(letra)

freq=[]

for j in lista:
    if j not in freq:
        freq.append(j)
        qtd=lista.count(j)
        print(f"letra: {j} - quantidade: {qtd}")
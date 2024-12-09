lista = []

for i in range(10):
    letra=input('informe a letra: ')
    lista.append(letra)

qtd_rep = []

for j in range(len(lista)):
    rep = lista.count(lista[j])
    qtd_rep.append(rep)



lista = []

for i in range(10):
    letra=input('informe a letra: ')
    lista.append(letra)

sem_rep = lista[:]

for j in sem_rep:
    if sem_rep.count(j)>1:
        sem_rep.remove(j)

for y in sem_rep:
    if sem_rep.count(y)>1:
        sem_rep.remove(y)

for x in sem_rep:
    print(f'a letra {x} aparece {lista.count(x)} vezes')


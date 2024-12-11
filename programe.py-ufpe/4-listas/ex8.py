letras=[]

for i in range(10):
    letra=input('informe a letra: ')
    letras.append(letra)

print(f'\nlista sem ordem: {letras}')

letras.sort()

print(f'\nnova lista em ordem: {letras}')

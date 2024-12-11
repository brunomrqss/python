letras = []

for i in range(10):
    letra=input(f'Informe a letra {i}: ') 
    letras.append(letra)
    
alterar = input('qual letra voce quer alterar? ')
nova = input('informe qual a nova letra: ')

for j in range(len(letras)):
    if letras[j]==alterar:
        letras[j]=nova
    
print(letras)
            
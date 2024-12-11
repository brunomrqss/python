letras = []

for i in range(5):
    letra=input()
    letras.append(letra)
    
pletra=input('letra? ')

if pletra in letras:
    print('o index é: ', letras.index(pletra))
else:
    print('a letra não está na lista')
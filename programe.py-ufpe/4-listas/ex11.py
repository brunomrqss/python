numeros=[]

for i in range(10):
    numero=int(input(f'informe o {i+1} numero: '))
    numeros.append(numero)

for j in range(len(numeros)):
    numeros.append(numeros[j]*2)

print(numeros)
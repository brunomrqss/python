numeros=[]

for i in range(10):
    numero=int(input(f'informe o {i+1} numero: '))
    numeros.append(numero)

for j in range(len(numeros)):
    numeros.append(numeros[j]*2)

count_remove=0
for j in numeros:
    if j%2==0:
        numeros.remove(j)
        count_remove+=1
    
print(f'A quantidade numeros pares excluídos foi de: {count_remove}')
print(f'Nova lista apenas com numeros impares: {numeros}')
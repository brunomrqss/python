numeros=[]

for i in range(10):
    numero=int(input('informe : '))
    numeros.append(numero)

pares_positivos=[]
impares_positivos=[]
pares_negativos=[]
impares_negativos=[]
zeros=[]

for j in numeros:
    if j%2==0 and j>0:
        pares_positivos.append(j)
    elif j%2==0 and j<0:
        pares_negativos.append(j)
    elif j%2!=0 and j>0:
        impares_positivos.append(j)
    elif j%2!=0 and j<0:
        impares_negativos.append(j)
    else:
        zeros.append(j)

print(f'Pares positivos: {pares_positivos}, quantidade: {len(pares_positivos)}')
print(f'Pares negativos: {pares_negativos}, quantidade: {len(pares_negativos)}')
print(f'Impares positivos: {impares_positivos}, quantidade: {len(impares_positivos)}')
print(f'Impares negativos: {impares_negativos}, quantidade: {len(impares_negativos)}')
print(f'Zeros: {zeros} , quantidade: {len(zeros)}')
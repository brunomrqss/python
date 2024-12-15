numeros = []

while len(numeros) < 10:

    numero=int(input(f'informe um numero: '))

    if numero%2==0:
        if numero in numeros:
            print(f'Número repetido!')
        else:
            numeros.append(numero)
    else:
        print(f'Número inválido!')

count_pares=0
lista_pares=[]

for j in numeros:
    if j%2==0:
        lista_pares.append(j)

for i in lista_pares:
    if len(str(i))==2:
        count_pares+=1

print(f'Os numeros pares com 2 casas são {lista_pares}')
print(f'A quantidade de numeros com duas casas é de {count_pares}')
    

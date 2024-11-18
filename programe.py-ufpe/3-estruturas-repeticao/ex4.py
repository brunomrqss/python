primeiro = int(input('primeiro numero de uma sequencia: '))
ultimo = int(input('ultimo numero de uma sequencia: '))

quantidade = 0
impares = 0 
pares = 0

soma_impares = 0
soma_pares = 0 

if primeiro < ultimo:
    for i in range(primeiro, ultimo):
        print(i)
        if i%2==0:
            pares+=1
            soma_pares += i
        else:
            impares+=1
            soma_impares += i

if primeiro > ultimo:
    for i in range(primeiro, ultimo, -1):
        print(i)
        if i%2==0:
            pares+=1
            soma_pares += i
        else:
            impares+=1
            soma_impares += i

quantidade = pares + impares + 1
print(quantidade)    
print(impares)
print(pares)
print(soma_pares)
print(soma_impares)
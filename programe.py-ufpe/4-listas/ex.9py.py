numeros=[]

for i in range(10):
    numero=int(input('informe : '))
    numeros.append(numero)

lista_par=[]
lista_impar=[]
lista_final=[]

for j in numeros:
    if j%2==0:
        lista_par.append(j)
    else:
        lista_impar.append(j)
        
lista_final = lista_par + lista_impar 

print(f'Nova sequencia: {lista_final}')
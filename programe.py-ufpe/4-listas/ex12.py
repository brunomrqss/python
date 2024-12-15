lista = [] #Instancia lista

for i in range(10):
    num = int(input(f"Digite o {i+1}° número: ")) #Recebe o número
    lista.append(num) #Insere em lista

nova_lista = lista.copy() #Instancia a nova lista de 20 números, cujos 10 primeiros são os número recebidos na entrada

for j in range(10):
    nova_lista.append(lista[j]*2) #Adiciona o dobro de cada um dos 10 primeiros números ao final da nova lista

count = 0 #Instancia o contador dos números pares removidos

for num in nova_lista:
    if num % 2 == 0: #Se o número for par
        nova_lista.remove(num) #Remove o número
        count = count + 1 #Incrementa 1 no contador

print(f"Foram removidos {count} número(s) pares da lista")
print(f"A lista alterada é: {nova_lista}")


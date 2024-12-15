lista_produtos=[]
preco_compra=[]
lucro_venda=[]
preco_venda=[]

stop=0

while stop < 3:

    nome_produto=input(f'informe o nome do produto: ')

    if nome_produto not in lista_produtos:
        lista_produtos.append(nome_produto)

        preco=float(input('Informe o preco de compra: '))
        preco_compra.append(preco)

        lucro=float(input('Informe a porcentagem de lucro sobre este item: '))
        lucro_venda.append(lucro)
    else:
        print('Produto já está incluso na lista de compras. Tente novamente.')
    
    stop+=1

for i in range(len(preco_compra)):
    lucro=(lucro_venda[i]/100)+1.0
    preco_venda.append(preco_compra[i]*lucro)


for j in range(len(lista_produtos)):
    print(f'O item {lista_produtos[j]} foi comprado por R${preco_compra[j]} e vendido por R${preco_venda[j]} com uma margem de lucro de {lucro_venda[j]}%')    

    
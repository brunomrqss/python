
operacao = input('Escolha uma operação (M) multiplicação - (A) adição: ')
count=1

if operacao == 'M':
    for i in range(1, 11):
        for j in range(1, 11):
            print(f'{j} * {count} = {j * count}')
        
        count+=1

if operacao == 'A':
    for i in range(1, 11):
        for j in range(1, 11):
            print(f'{j} + {count} = {j + count}')
    
        count +=1 
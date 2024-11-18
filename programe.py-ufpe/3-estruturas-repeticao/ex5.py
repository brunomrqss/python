numero = int(input('informe um numero inteiro e positivo: '))
cubo = float(input('tente informar o cubo deste numero: '))


n_digitados = 1
n_maiores = 0
n_menores = 0

while numero**3 != cubo:
    n_digitados += 1
    cubo = int(input('tente novamente informar o numero do cubo: '))
    if cubo > numero:
        n_maiores +=1 
        print(f'o cubo informado é maior que o numero')
    else:
        n_menores +=1
        print(f'o cubo informado é menor que o numero')

if numero**3 == cubo: 
    print(f'Parabéns você acertou o número!')
    print(f'Cubos digitados maiores que o número: {n_maiores}')
    print(f'Cubos digitados menores que o número: {n_menores}')



    

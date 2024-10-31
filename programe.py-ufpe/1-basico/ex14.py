numero = int(input('numero: '))

unidade = numero%10 
dezena = (numero//10)%10
centena = (numero//100)

print(f'unidade: {unidade}\ndezena: {dezena}\ncentena: {centena}')
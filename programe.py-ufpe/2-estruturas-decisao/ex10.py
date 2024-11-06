descricao = input()
tipo = input()
valor = int(input())

valor_reajustado = 0

if tipo not in ('A', 'B', 'C', 'D', 'E'):
    print('Tipo não encontrado, tente novamente: ')
    tipo=input('Informe um tipo válido: ')
    if tipo in ('A', 'B', 'C', 'D', 'E'):
            if tipo in ('A', 'B'):
                valor_reajustado = valor * ((100 - 12.3) / 100)
            elif tipo == 'C':
                valor_reajustado = valor * ((100 - 14) / 100)
            elif tipo in ('D', 'E'):
                valor_reajustado = valor * ((100 - 15.7)/100)

print(f"Valor após reajuste: R${valor_reajustado:.2f}")
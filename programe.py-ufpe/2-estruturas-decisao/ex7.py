primeiro_nome = input()
sobrenome = input()
idade = int(input())

if idade < 12:
    print(primeiro_nome + ' ' + sobrenome)
    print('Categorial Infantil')
elif idade >= 13 and idade <= 17:
    print(primeiro_nome + ' ' + sobrenome)
    print('Categoria Juvenil')
elif idade >= 18 and idade <= 35:
    print(primeiro_nome + ' ' + sobrenome)
    print('Categoria Adulto')
else:
    print(primeiro_nome + ' ' + sobrenome)
    print('Categoria master')
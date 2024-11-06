caractere = input()

if caractere in ('a', 'e', 'i', 'o', 'u'):
    print('vogal')

if caractere in ('*', '+', '-', '/'):
    print('operação matemática')

if ord(caractere) >= 48 and ord(caractere) <= 54:
    print('numeral')
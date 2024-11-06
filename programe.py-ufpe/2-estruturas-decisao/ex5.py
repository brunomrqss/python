n1 = input()
operacao = input()
n2 = input()


resultado = 0

if operacao == '*':
    resultado = int(n1)*int(n2)
    print(resultado)
elif operacao == '+':
    resultado = int(n1)+int(n2)
    print(resultado)
elif operacao == '-':
    resultado = int(n1)-int(n2)
    print(resultado)
else:
    resultado = int(n1)/int(n2)
    print(resultado)


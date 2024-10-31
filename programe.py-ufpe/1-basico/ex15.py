var1 = int(input(''))
var2 = int(input(''))
var_aux = var1

print(f'antes da troca\nvar1={var1}\nvar2={var2}')

var1=var2
var2=var_aux

print(f'depois da troca\nvar1={var1}\nvar2={var2}')
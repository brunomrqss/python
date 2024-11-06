num1=int(input())
num2=int(input())
num3=int(input())

maior_num = num1 
medio_num = num1 
menor_num = num1

if num2 < menor_num: 
    menor_num = num2

if num3 < menor_num: 
    menor_num = num3 

if num2 > maior_num: 
    maior_num = num2

if num3 > maior_num:
    maior_num = num3 

if num2 > menor_num and num2 < maior_num:
    medio_num = num2

if num3 > menor_num and num3 < maior_num:
    medio_num = num3

print(maior_num, medio_num, menor_num)
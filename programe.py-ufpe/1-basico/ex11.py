'''
Crie um programa que receba uma temperatura em Celsius e, considerando as seguintes 
fórmulas K=C+273 e F=1,8C+32, exiba a temperatura lida 
usando as escalas Kelvin (K) e Fahrenheit (F).
'''

temp_celsius = int(input("temperatura em celsius: "))

temp_fahrenheit = (1.8*temp_celsius)+32
temp_kelvin = temp_celsius+273

print(f"{temp_celsius}ºC em Fahrenheint é {temp_fahrenheit}F e em Kelvin {temp_kelvin}K")
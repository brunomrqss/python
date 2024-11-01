import math

print(math.pi)
print(math.pow(5, 15))
print(type(int('101')))
print(round(math.pi, 2))

#part 1
radius = int(input())
volume = (3/4) * math.pi * (math.pow(radius, 3))
print(f'{volume:.1f}cm³')

#part 2
x = 2
sum_squared = (math.cos(x)**2) + (math.sin(x)**2)
# print(math.pow(math.cos(x), 2) + math.pow(math.sin(x), 2)) -> outra alternativa
print(sum_squared)

#part 3
print(math.e**2)
print(math.pow(math.e,2))
print(math.exp(x))

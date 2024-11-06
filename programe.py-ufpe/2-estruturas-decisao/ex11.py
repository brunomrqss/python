n1 = int(input())
n2 = int(input())

if n1 % n2 == 0 and n1 % 2 == 0 and n2 % 2 == 0:
    print(f'Sim, {n1} é divisível por {n2} e ambos são pares.')
elif n1 % n2 == 0 and not n1 % 2 == 0 and n2 % 2 == 0:
    print(f"Sim, {n1} é divisível por {n2} mas um deles não é par.")
else:
    print("N1 não é divisível de N2")
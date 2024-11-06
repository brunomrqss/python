def is_triangle(n1, n2, n3):
    if (n1+n2) > n3 or (n1+n3) > n2 or (n2+n3) > n1:
        print("Sim")
    else:
        print("Não")

is_triangle(1, 2, 4)
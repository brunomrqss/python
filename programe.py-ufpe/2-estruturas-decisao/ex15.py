seg1 = int(input("Digite o comprimento do primeiro segmento: "))
seg2 = int(input("Digite o comprimento do segundo segmento: "))
seg3 = int(input("Digite o comprimento do terceiro segmento: "))

# Verifica se os segmentos podem formar um triângulo
if (seg1 + seg2 > seg3) and (seg2 + seg3 > seg1) and (seg1 + seg3 > seg2):
    # Determina o tipo de triângulo
    if seg1 == seg2 == seg3:
        print("Triângulo equilátero")
    elif seg1 != seg2 and seg1 != seg3 and seg2 != seg3:
        print("Triângulo escaleno")
    else:
        print("Triângulo isósceles")
else:
    print("Os segmentos não podem formar um triângulo.")

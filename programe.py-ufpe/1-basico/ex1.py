nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))

dif_nota1 = 10 - nota1 
dif_nota2 = 10 - nota2 

media = (nota1 + nota2) / 2

dif_media = 10 - media

print(f"Distância da nota 1 em relação ao 10: {dif_nota1:.2f} pontos")
print(f"Distâcia da nota 2 em relação ao 10: {dif_nota2:.2f} pontos")
print(f"Média do aluno: {media:.2f}")
print(f"Distância da média em relação a média 10: {dif_media:.2f} pontos")
valor_venda=float(input("digite o valor de venda do produto: "))
desconto=int(input("porcentual de desconto: "))/100

print(f"Valor do produto é de R${valor_venda}")
valor_descontado = valor_venda * desconto
print(f"Valor com desconto é de R${valor_venda-valor_descontado}")


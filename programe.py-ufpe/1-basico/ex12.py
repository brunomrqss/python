qtd_ingressos = 6789
valor_inteira = 123.45 
valor_meia = valor_inteira/2

qtd_vendidos_meia = 6789 * 0.45 
qtd_vendidos_inteira = 6789 * 0.55

print(f"Quantidade de ingressos vendidos meia entrada: {qtd_vendidos_meia:.0f}")
print(f"Quantidade de ingressos vendidos inteira: {qtd_vendidos_inteira:.0f}")

faturamento_meia = qtd_vendidos_inteira * valor_meia
faturamento_inteira = qtd_vendidos_inteira * valor_inteira

print(f"Faturamento ingressos meia entrada: R${faturamento_meia:.2f}")
print(f"Faturamento ingressos inteira: R${faturamento_inteira:.2f}")

faturamento_total = faturamento_meia + faturamento_inteira

print(f"Total faturamento: R${faturamento_total:.2f}")
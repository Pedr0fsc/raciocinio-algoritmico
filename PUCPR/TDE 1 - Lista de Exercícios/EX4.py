"""
Faça um algoritmo que recebe o valor de um produto e calcule os seguintes valores:
(1) a vista com 5% de desconto; (2) o valor da parcela em 2x; (3) o valor da parcela
em 3x com acréscimo de 5%.
"""

produto = float(input("Insira o valor do produto: "))
produto_5_desconto = round(produto - (produto * 0.05), 2)
produto_2_parcelas = round(produto / 2, 2)
produto_3_parcelas_5_acrescimo = round((produto + (produto * 0.05)) / 3, 2)

print("Valor do produto:", produto, "\nVocê possui as seguintes opções de pagamento:")
print("1 - A vista com 5% de desconto: R$",produto_5_desconto)
print("2 - Parcelado em 2x: R$",produto_2_parcelas)
print("3 - Parcelado em 3x com 5% de acréscimo: R$",produto_3_parcelas_5_acrescimo)
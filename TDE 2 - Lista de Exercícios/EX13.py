"""
Em uma determinada loja de eletrodomésticos, os produtos podem ser adquiridos da
seguinte forma:
Elabore um algoritmo que leia a opção do cliente e o preço de tabela do produto, mostrando
então o valor calculado conforme a condição escolhida.
"""
print("Opções  |          Condição         |       Cálculo\n1       |           à vista         |       8% de desconto\n2       |       em 2 parcelas       |       4% de desconto, dividido em duas vezes\n3       |       em 3 parcelas       |       sem desconto, dividido em três vezes\n4       |       em 4 parcelas       |       4% de desconto, dividio em 4 parcelas\n")

opcao = int(input("Informe uma opção de compra: "))
produto = float(input("Informe o valor do produto: "))
total = float
parcelas = int

match opcao:
    case 1:
        total = (produto - (produto * 0.08))
        parcelas = "à vista"
        print("\nTotal da compra: R$", total, "\nParcelas: ", parcelas)
    case 2:
        total = (produto - (produto * 0.04)) / 2
        parcelas = opcao
        print("\nTotal da compra: R$", total, "\nParcelas: ", parcelas)
    case 3:
        total = (produto - (produto / 3))
        parcelas = opcao
        print("\nTotal da compra: R$", total, "\nParcelas: ", parcelas)
    case 4:
        total = (produto - (produto * 0.04 / 4))
        parcelas = opcao
        print("\nTotal da compra: R$", total, "\nParcelas: ", parcelas)
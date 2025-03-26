"""
Uma empresa de câmbio permite a compra de dólares, libras e euros. Elabore um
algoritmo que leia o código da moeda que o cliente quer comprar e qual o montante
que ele quer adquirir nessa moeda. Mostre então quanto ele deverá pagar em reais
para concretizar a operação. Além da cotação, a empresa cobra uma comissão de 5%
(quando o valor for menor que R$ 1.000), ou de 3% (quando maior ou igual a
R$1.000). Considere o câmbio do dia.
"""
repeat = 1

while repeat == 1:
    print("'1' -> Dólar($) = R$5,70\n'2' -> Libras(£) = R$7,35\n'3' -> Euro(€) = R$6,15")
    option = int(input("Insira qual opção de compra você quer escolher: "))
    qtd = float(input("Insira a quantidade que você quer comprar dessa moeda: "))

    total = float

    match option:
        case 1:
            total = qtd * 5.70
        case 2:
            total = qtd * 7.35
        case 3:
            total = qtd * 6.15

    if total < 1000:
        total_comissao = round(total + (total * 0.05), 2)
        print("Total: R$", total_comissao, " --> R$", total, "+ 5% de comissão")
    else:
        total_comissao = round(total + (total * 0.03), 2)
        print("Total: R$", total_comissao, " --> R$", total, "+ 3% de comissão")
    
    repeat = int(input("Deseja continuar(1 -> sim / 0 -> não): "))
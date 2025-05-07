# Leia dois valores reais do teclado, calcular e imprimir na tela:
# a) A soma destes valores
# b) O produto deles
# c) O quociente entre eles

n1 = float(input("Entre com o primeiro número: "))
n2 = float(input("Entre com o segundo número: "))

soma = round(n1 + n2, 2)
produto = round(n1 * n2, 2)
quociente = round(n1 / n2, 2)

print(".\n.\n.\nOs números inseridos foram", n1, "e", n2, "\nA soma desses números é: ", soma, "\nO produto desses números é: ", produto, "\nO quociente entre esses números é: ", quociente)
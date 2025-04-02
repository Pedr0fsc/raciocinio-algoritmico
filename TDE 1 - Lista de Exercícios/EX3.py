# Faça um algoritmo que receba o salário de um profissional e calcule quantos salário mínimos ele recebe.

salario_minimo = 1518
salario_recebido = float(input("Insira quanto você recebe: "))
qtd_salarios_minimos = round(salario_recebido/salario_minimo, 2)

print("O seu salário atual é equivalente à", qtd_salarios_minimos, "salários mínimos")
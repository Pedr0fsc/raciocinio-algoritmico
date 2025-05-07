# Ler 4 números inteiros e calcular a soma dos que forem par.

nums_par = []

for i in range(4):
    num = int(input("Entre com um número: "))
    if num % 2 == 0:
        nums_par.append(num)
    i += 1

print("A soma dos números pares inseridos é:", sum(nums_par))
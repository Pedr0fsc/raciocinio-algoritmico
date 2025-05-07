# Construa a tabela de multiplicação de 1 a 10 utilizando apenas um laço de repetição.

for n1 in range(1, 11):
    for n2 in range(1, 11):
        print(f"{n1} x {n2} = {n1 * n2}")
    print()
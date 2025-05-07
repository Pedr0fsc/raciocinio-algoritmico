# Construa a tabela de multiplicação de 1 a 10. (Ex: 1x1 = 1, 1x2=2, 10x10 =100)

for n1 in range(1, 11):
    for n2 in range(1, 11):
        print(f"{n1} x {n2} = {n1 * n2}")
    print()
    
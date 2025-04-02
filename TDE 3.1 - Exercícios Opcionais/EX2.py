"""
Dizemos que um número natural é triangular se ele é produto de três números naturais consecutivos.
Exemplo: 120 é triangular, pois 4.5.6 = 120. Dado um inteiro não-negativo n, verificar se n é
triangular.
"""

num = int(input("Digite um número: "))

if num >= 0:
    #code
    t = ((8 * num) + 1) ** 0.5
    if int(num) == num:
        print(t)
else:
    print("Digite um número inteiro não negativo")
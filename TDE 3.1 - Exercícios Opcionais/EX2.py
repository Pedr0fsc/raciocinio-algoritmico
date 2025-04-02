"""
Dizemos que um número natural é triangular se ele é produto de três números naturais consecutivos.
Exemplo: 120 é triangular, pois 4.5.6 = 120. Dado um inteiro não-negativo n, verificar se n é
triangular.
"""

def eh_triangular(n):
    if n < 0:
        return False
    
    i = 1
    while i * (i + 1) * (i + 2) <= n:
        if i * (i + 1) * (i + 2) == n:
            return True
        i += 1
    return False

try:
    n = int(input("Digite um número inteiro não negativo: "))
    if n >= 0:
        if eh_triangular(n):
            print(f"{n} é um número triangular.")
        else:
            print(f"{n} não é um número triangular.")
    else:
        print("Por favor, insira um número não negativo.")
except ValueError:
    print("Entrada inválida. Por favor, insira um número inteiro.")

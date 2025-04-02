"""
Faça um programa que mostre os n termos da Série a seguir:
S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
No final, mostre a soma também.
"""

def calcular_serie(n):
    soma = 0
    termos = []
    
    for i in range(1, n + 1):
        termo = i / (2 * i - 1)
        soma += termo
        termos.append(f"{i}/{2 * i - 1}")
    
    serie_formatada = " + ".join(termos)
    print(f"Série: {serie_formatada}")
    print(f"Soma total: {soma:.4f}")

try:
    n = int(input("Digite o número de termos da série: "))
    if n > 0:
        calcular_serie(n)
    else:
        print("Por favor, insira um número positivo.")
except ValueError:
    print("Entrada inválida. Por favor, insira um número inteiro positivo.")
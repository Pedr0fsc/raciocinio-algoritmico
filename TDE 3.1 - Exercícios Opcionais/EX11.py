"""
Sendo H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, faça um programa que calcule o valor de H com N termos.
"""

def calcular_serie(n):
    soma = 0
    termos = []
    
    for i in range(0, n):
        termo = 1 / (i + 1)
        soma += termo
        termos.append(f"{1}/{i + 1}")
    
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

"""
Elabore um algoritmo que leia um número inteiro e mostre sua raiz quadrada (informe
“Valor inválido” para números negativos).
"""

import math

num = int(input("Insira um número inteiro: "))

if(num >= 0):
    sqr = math.sqrt(num)
    print("A raiz quadrada desse número é igual a",sqr)
else:
    print("Não é possível calcular a raiz quadrada de números negativos")
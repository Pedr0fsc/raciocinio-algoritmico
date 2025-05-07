# Escreva um programa que leia um vetor de números inteiros de 10 posições, aceitando apenas
# valores positivos. Modifique então o vetor de forma que, tenhamos primeiro todos os números pares,
# depois, os números impares. Mostre o vetor antes de depois da modificação.

import random

nums = []
nums_pares = []
nums_impares = []

for i in range(10):
    num = random.randint(0, 10)
    if num % 2 == 0:
        nums_pares.append(num)
    else:
        nums_impares.append(num)
    i += 1

nums = nums_pares + nums_impares
print(nums)
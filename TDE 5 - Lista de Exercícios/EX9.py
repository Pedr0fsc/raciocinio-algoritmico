# Desenvolva um programa que leia 10 números inteiros e armazene-os em um vetor chamado vLido.
# Depois, crie dois outros vetores: vPares, contendo somente os números pares de vLido, e vImpares
# contendo somente os números ímpares de vLido. Os vetores vPares e vLido não deverão conter
# zeros. Mostre então os três vetores.

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
    nums.append(num)
    i += 1

print(f"Vetor principal: {nums}")
print(f"Vetor dos números pares: {nums_pares}")
print(f"Vetor dos números ímpares: {nums_impares}")
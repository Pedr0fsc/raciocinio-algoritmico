"""
Elabore um algoritmo que leia um conjunto de 10 números inteiros. Mostre então
qual o valor da soma e da média aritmética do conjunto.
"""
import random

nums = []

for i in range(0, 10):
    rand_int = random.randint(0, 100)
    nums.append(rand_int)

print("Lista de 10 números inteiros: ", nums)
print("Soma desses números: ", sum(nums))
print("Média desses números: ", sum(nums) / nums.__len__())
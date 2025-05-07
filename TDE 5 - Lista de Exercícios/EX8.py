# Elabore um programa que leia um vetor de 10 posições inteiras. Depois, solicite para o usuário um
# número que ele gostaria de pesquisar neste vetor, caso o número exista no vetor, mostre em qual(is)
# posição(ões) ele foi encontrado e quantas ocorrências foram detectadas.

import random

nums = []
target = int(input("Digite um número que você gostaria pesquisar no vetor (de 0 a 10): "))
position = []
ocorrencies = 0

for i in range(10):
    num = random.randint(0, 10)
    nums.append(num)
    i += 1

for i in range(len(nums)):
    if nums[i] == target:
        ocorrencies += 1
        position.append(i)

print(nums)
if ocorrencies > 0:
    print(f"O número {target} foi encontrado {ocorrencies} vezes na posição {position} (0 a 9)")
else:
    print(f"O número {target} não foi encontrado no vetor")

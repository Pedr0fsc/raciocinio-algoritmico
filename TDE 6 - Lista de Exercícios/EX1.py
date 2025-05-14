# Desenvolva um programa que leia uma matriz quadrada de números inteiros de dimensão (4×4), e
# então coloque em um outro vetor de 4 posições o maior valor encontrado na coluna da matriz cujo
# índice é o mesmo do vetor, ou seja, o maior valor da coluna zero da matriz na posição zero do vetor e
# assim por diante. Mostre então a matriz, o vetor e a média aritmética do vetor.

import random

m = []
v = []

for i in range(0, 4):
    linha_m = []
    for j in range(0, 4):
        linha_m.append(random.randint(0, 9))
    m.append(linha_m)
    maior = max(linha_m)
    v.append(maior)

print("Matriz: ")
for i in range(len(m)):
    for j in range(len(m[0])):
        print(m[i][j], end = ' | ')
    print()

print(v)
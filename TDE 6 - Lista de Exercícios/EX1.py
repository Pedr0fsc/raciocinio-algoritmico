# Desenvolva um programa que leia uma matriz quadrada de números inteiros de dimensão (4×4), e
# então coloque em um outro vetor de 4 posições o maior valor encontrado na coluna da matriz cujo
# índice é o mesmo do vetor, ou seja, o maior valor da coluna zero da matriz na posição zero do vetor e
# assim por diante. Mostre então a matriz, o vetor e a média aritmética do vetor.

import random

m = []

for i in range(0, 4):
    linha_m = []
    for j in range(0, 4):
        linha_m.append(random.randint(0, 9))
    m.append(linha_m)

v = []
for col in range(4):
    maior = m[0][col]
    for lin in range(1, 4):
        if m[lin][col] > maior:
            maior = m[lin][col]
    v.append(maior)

print("Matriz: ")
for i in range(len(m)):
    for j in range(len(m[0])):
        print(m[i][j], end = ' | ')
    print()

print("Vetor com o maior elemento de cada coluna: ", v)

med = sum(v) / len(v)
print("Média aritmética do vetor: ", med)
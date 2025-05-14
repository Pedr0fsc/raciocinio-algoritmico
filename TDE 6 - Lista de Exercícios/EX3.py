# Elabore um programa que preencha uma matriz quadrada (4x4) de números inteiros, sorteados dentro
# do intervalo 100 a 999, garantindo que não haverá nenhuma repetição (os 16 números devem ser
# únicos). Encontre então o valor do menor elemento da linha em que se encontra o maior elemento da
# matriz. Mostre a matriz e os dois valores encontrados.

import random

matriz = []

for i in range(4):
    linha_matriz = []
    for j in range(4):
        linha_matriz.append(random.sample(range(100, 999), 1))
    matriz.append(linha_matriz)

maior_elemento = matriz[0][0]
maior_linha = 0

for i in range(4):
    for j in range(4):
        if matriz[i][j] > maior_elemento:
            maior_elemento = matriz[i][j]
            maior_linha = i

menor_elemento = matriz[maior_linha][0]
for j in range(4):
        if matriz[maior_linha][j] < menor_elemento:
            menor_elemento = matriz[maior_linha][j]

print("Matriz: ")
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j], end = ' | ')
    print()

print(f"O maior valor é {maior_elemento} que está localizado na linha {maior_linha}")
print(f"O menor valor dessa linha é {menor_elemento}")
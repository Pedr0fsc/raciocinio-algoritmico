# Escreva um programa que preencha uma matriz quadrada de números inteiros de dimensão (5×5)
# com valores inteiros (dentro do intervalo 10 a 99). Para cada uma das figuras abaixo (elabore quatro
# versões do programa): mostre a matriz original, mostre a matriz apenas com os valores que estão na
# parte hachurada e mostre a soma destes valores:

import random

matriz = []

for i in range(5):
    linha_matriz = []
    for j in range(5):
        linha_matriz.append(random.sample(range(10, 99), 1))
    matriz.append(linha_matriz)

print("Matriz Original: ")
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j], end = ' | ')
    print()

print("Matriz Versão A: ")
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if i == 2 or j == 2:
            print(matriz[i][j], end = ' | ')
        else:
            print("  - ", end = ' | ')
    print()

print("Matriz Versão B: ")
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if i == 0 or i == 4 or j == 0 or j == 4:
            print(matriz[i][j], end = ' | ')
        else:
            print("  - ", end = ' | ')
    print()

print("Matriz Versão C: ")
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if j - i == 1 or i - j == 1:
            print(matriz[i][j], end = ' | ')
        else:
            print("  - ", end = ' | ')
    print()

print("Matriz Versão D: ")
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if j - i == 1 or i - j == 1 or j - i == 3 or i - j == 3:
            print(matriz[i][j], end = ' | ')
        else:
            print("  - ", end = ' | ')
    print()
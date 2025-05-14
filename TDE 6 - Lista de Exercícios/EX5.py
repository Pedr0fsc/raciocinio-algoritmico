# Escreva um programa que popule uma matriz (15×7) de números inteiros sorteados dentro do
# intervalo 10 a 99. Modifique então a matriz de forma que, caminhando da esquerda para a direita, de
# cima para baixo, tenhamos primeiro todos os números pares, depois, os números impares. Mostre a
# matriz antes e depois da modificação.

import random

matriz = []

for i in range(15):
    linha_matriz = []
    for j in range(7):
        linha_matriz.append(random.randint(10, 99))
    matriz.append(linha_matriz)

print("Matriz: ")
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j], end = ' | ')
    print()

pares = []
impares = []

for lin in matriz:
    for num in lin:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)

nova_matriz = []
todos_os_numeros = pares + impares

k = 0
for i in range(15):
    linha_matriz = []
    for j in range(7):
        linha_matriz.append(todos_os_numeros[k])
        k += 1
    nova_matriz.append(linha_matriz)

print("Matriz organizada em Pares e Ímpares: ")
for i in range(len(nova_matriz)):
    for j in range(len(nova_matriz[0])):
        print(nova_matriz[i][j], end = ' | ')
    print()
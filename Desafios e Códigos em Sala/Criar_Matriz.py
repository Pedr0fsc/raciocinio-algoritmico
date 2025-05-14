import random

matriz = []

linhas = int(input("Informe a quantidade de linhas: "))

colunas = int(input("Informe a quantidade de colunas: "))

for i in range(linhas):
    linha_matriz = []
    for j in range(colunas):
        linha_matriz.append(random.randint(0, 9))
    matriz.append(linha_matriz)

print("Matriz: ")
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j], end = ' | ')
    print()

print("Diagonal: ")
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if i == j:
            print(matriz[i][j], end = ' | ')
        else:
            print("-", end = ' | ')
    print('')

print("Triângulo Superior: ")
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if i < j:
            print(matriz[i][j], end = ' | ')
        else:
            print("-", end = ' | ')
    print('')

print("Triângulo Inferior: ")
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        if i > j:
            print(matriz[i][j], end = ' | ')
        else:
            print("-", end = ' | ')
    print('')
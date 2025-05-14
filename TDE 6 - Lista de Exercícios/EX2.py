# Implemente um programa que permita multiplicar uma matriz de ordem (3×3) de números inteiros
# fornecida pelo usuário por um número também fornecido pelo usuário.
# Lembrete: para multiplicar uma matriz Am×n por um escalar k, basta multiplicar cada entrada aij
# de A por k. Assim, a matriz resultante B será também da ordem (m×n) e bij = k * aij.

m = []

for i in range(3):
    linha_matriz = []
    for j in range(3):
        linha_matriz.append(int(input("Informe um número para a matriz: ")))
    m.append(linha_matriz)

multiplicador = int(input("Informe o número multiplicador: "))

m_multiplicada = []
for lin in range(3):
    nova_lin = []
    for col in range(3):
        nova_lin.append(m[lin][col] * multiplicador)
    m_multiplicada.append(nova_lin)

print("Matriz Original: ")
for i in range(len(m)):
    for j in range(len(m[0])):
        print(m[i][j], end = ' | ')
    print()

print("Matriz Multiplicada: ")
for i in range(len(m)):
    for j in range(len(m[0])):
        print(m_multiplicada[i][j], end = ' | ')
    print()
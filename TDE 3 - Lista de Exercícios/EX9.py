"""
Imprima os números múltiplos de 3 entre li (limite inicial) e lf (limite final). Os
valores inteiros de li e lf devem ser informados pelo usuário e não pertencem ao
intervalo, ou seja, intervalo aberto.
"""

li = int(input("Insira o limite inicial: "))
lf = int(input("Insira o limite final: "))

for i in range(li + 1, lf):
    if i % 3 == 0:
        print(i)
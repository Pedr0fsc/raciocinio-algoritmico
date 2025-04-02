"""
Faça um programa que leia uma quantidade indeterminada de números positivos, encerrando quando
a entrada for -1 e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-
100].
"""
import random

interval_0_25 = []
interval_26_50 = []
interval_51_75 = []
interval_76_100 = []

i = random.randint(0, 30)

for i in range(1, i + 1):
    num = random.randint(0, 100)
    if num >= 0 and num < 26:
        interval_0_25.append(num)
    elif num >= 26 and num < 51:
        interval_26_50.append(num)
    elif num >= 51 and num < 76:
        interval_51_75.append(num)
    elif num >= 76 and num < 101:
        interval_76_100.append(num)

print("O intervalo de números entre 0 e 25 possui", len(interval_0_25), "membros, sendo eles: ", interval_0_25)
print("O intervalo de números entre 26 e 50 possui", len(interval_26_50), "membros, sendo eles: ", interval_26_50)
print("O intervalo de números entre 51 e 75 possui", len(interval_51_75), "membros, sendo eles: ", interval_51_75)
print("O intervalo de números entre 76 e 100 possui", len(interval_76_100), "membros, sendo eles: ", interval_76_100)


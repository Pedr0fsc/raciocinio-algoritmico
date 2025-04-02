"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5! = 5 x 4
x 3 x 2 x 1 = 120
"""

num = int(input("Digite um número inteiro: "))

def fatorial_calc(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

result = fatorial_calc(num)
print("O fatorial do número", num, "é", result)
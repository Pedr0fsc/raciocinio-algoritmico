"""
Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro
informado pelo usuário.
"""

upper = int(input("Informe um número limite: "))
prime_num = []

for num in range(1, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)

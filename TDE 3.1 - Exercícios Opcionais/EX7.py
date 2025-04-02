"""
Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia.
Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que
peça um número inteiro e determine se ele é ou não um número primo.
"""

num = int(input("Digite um número: "))
flag = False

if num == 0 or num == 1:
    print(num, "não é um número primo!")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break

if flag:
    print(num, "não é um número primo!")
else:
    print(num, "é um número primo!")

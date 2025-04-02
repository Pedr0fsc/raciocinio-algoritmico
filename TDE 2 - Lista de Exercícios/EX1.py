# Elabore um algoritmo que leia um número inteiro e verifique se ele é par ou ímpar.

num = int(input("Insira um número inteiro: "))
res = num % 2

if(res == 0):
    print("Esse número é par!")
else:
    print("Esse número é ímpar!")
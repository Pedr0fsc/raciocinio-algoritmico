"""
Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número
elevado ao segundo número. Não utilize a função de potência da linguagem.
"""
base = int(input("Digite o número base: "))
expoente = int(input("Digite o número expoente: "))

for expoente in range(1, expoente):
    base *= base
print(base)
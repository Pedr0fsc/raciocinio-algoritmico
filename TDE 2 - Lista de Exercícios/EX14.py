#Escreva um algoritmo que leia três números inteiros e mostre o valor do maior deles.

n1 = int(input("Insira o 1° número: "))
n2 = int(input("Insira o 2° número: "))
n3 = int(input("Insira o 3° número: "))

def switch(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        print("O maior número é ", n1)
    elif n2 > n1 and n2 > n3:
        print("O maior número é ", n2)
    elif n3 > n1 and n3 > n2:
        print("O maior número é ", n3)

print(switch(n1, n2, n3))
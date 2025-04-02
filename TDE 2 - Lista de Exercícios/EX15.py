# Escreva um algoritmo que leia três números inteiros e mostre-os em ordem decrescente.

n1 = int(input("Insira o 1° número: "))
n2 = int(input("Insira o 2° número: "))
n3 = int(input("Insira o 3° número: "))

def switch(n1, n2, n3): #3!
    if n1 > n2 and n1 > n3 and n2 > n3:
        print(n1, n2, n3) #123
    elif n1 > n2 and n1 > n3 and n2 < n3:
        print(n1, n3, n2) # 132
    elif n2 > n1 and n2 > n3 and n1 > n3:
        print(n2, n1, n3) # 213
    elif n2 > n1 and n2 > n3 and n2 < n3:
        print(n2, n3, n1) # 231
    elif n3 > n1 and n3 > n2 and n1 > n2:
        print(n3, n1, n2) # 312
    elif n3 > n1 and n3 > n2 and n1 < n2:
        print(n3, n2, n1) # 321

print(switch(n1, n2, n3))
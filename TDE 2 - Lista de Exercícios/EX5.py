"""
Em uma determinada papelaria a fotocópia custa R$ 0,25, caso sejam tiradas menos de 100
cópias. A partir de 100 cópias, o valor de cada fotocópia tirada cai para R$ 0,20. Elabore
um algoritmo que leia o número de cópias e mostre o valor a pagar pelo serviço.
"""

num_fotocopia = int(input("Insira a quantdade de impressões a serem feitas: "))
preco_fotocopia = float
total = float

if(num_fotocopia < 100 and num_fotocopia > 0):
    preco_fotocopia = 0.25
    total = num_fotocopia * preco_fotocopia
    print("Valor: R$",preco_fotocopia)
    print("O total das impressões foi de R$",total)
elif(num_fotocopia >= 100):
    preco_fotocopia = 0.20
    total = num_fotocopia * preco_fotocopia
    print("Valor: R$",preco_fotocopia)
    print("O total das impressões foi de R$",total)
else:
    print("Valor inaquedado")
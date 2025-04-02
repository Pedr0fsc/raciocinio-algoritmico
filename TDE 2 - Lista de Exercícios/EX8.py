"""
Em um determinado estacionamento a primeira hora custa R$ 8,00, que é o valor mínimo
praticado. Após uma hora o valor é fracionado, R$ 1,50 a cada 15 minutos. Elabore um
algoritmo que leia um número inteiro correspondente a quantidade de minutos usados no
estacionamento e mostre a mensagem “Valor mínimo, R$ 8,00” ou “Valor fracionado, R$
x”, no qual x será o valor a pagar calculado pelo algoritmo.
"""

min = int(input("Insira quantos minutos você ficou estacionado: "))
preco = float

if(min <= 60 and min > 0):
    preco = 8
    print("Valor mínimo: R$", preco)
elif(min > 60 and min > 0):
    preco = round((min / 15) * 1.50, 2)
    print("Valor fracionado: R$",preco)
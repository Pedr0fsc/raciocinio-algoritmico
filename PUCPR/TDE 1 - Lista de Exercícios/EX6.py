"""
Faça um algoritmo que calcule a quantidade de latas de tintas necessárias para pintar
um tanque cilindro, em que são fornecidas sua altura e raio, sabendo que:
a. A lata de tinta custa R$ 50,00
b. Cada lata contém 5 litros
c. Cada litro de tinta pinta 3 metros quadrados
d. Entrada do programa: altura e raio do cilindro
e. Saída: valor em reais e quantidade de latas
"""

raio = float(input("insira o raio da base do cilindro para pintura: "))
altura = float(input("Insira o valor da altura do cilindro: "))

area_cilindro = (3.14 * raio ** 2) * altura
latas = area_cilindro / 15
preco_lata = latas * 50

print("A pintura do seu cilindro de ",area_cilindro,"m² custou R$",preco_lata,"e",latas,"latas de tinta")
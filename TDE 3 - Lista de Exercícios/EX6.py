"""
Imprima uma tabela de conversão de polegadas para centímetros, cuja escala vai de
1 a 20 polegadas. A conversão entre estas duas unidades é dada por: polegada =
centímetro × 2,54
"""
pol = 0

for x in range(1, 21):
    pol += 1
    cm = pol * 2.54
    print("Polegadas: ", pol, "in  /  Centímetro: ", cm, "cm")
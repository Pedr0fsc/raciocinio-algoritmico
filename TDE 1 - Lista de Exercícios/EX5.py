"""
Faça um algoritmo que calcule o consumo médio de um automóvel (medido em
km/l), solicitando como entrada a distância total percorrida (KM) e o volume de
combustível consumido para percorre-la (litros).
"""

km_percorridos = float(input("Insira quantos KM foram percorridos: "))
combustivel = float(input("Insira quantos litros de combustível foram consumidos: "))

consumo_medio = round(km_percorridos/combustivel, 1)

print("O consumo médio do automóvel foi de", consumo_medio,"km/l")
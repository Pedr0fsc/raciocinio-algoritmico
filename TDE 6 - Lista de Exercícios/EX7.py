# Considerando a mesma tabela da questão anterior, desenvolva um programa que permita ao usuário
# informar várias cidades em sequência, até inserir um código finalizador. Mostre então as cidades que
# compõem o roteiro fornecido, a distância de cada percurso intermediário e a distância total do roteiro
# fornecido.

cidades = ["Curitiba (0)", "Florianópolis (1)", "Porto Alegre (2)", "São Paulo (3)", "Rio de Janeiro (4)"]
print(f"{cidades}\n")
percurso = int(input("Informe as cidades que você vai visitar: "))

matriz = [[" - ", 310, 716, 408, 852],
          [310, " - ", 470, 705, 1144],
          [716, 470, " - ", 1119, 1553],
          [408, 705, 1119, " - ", 429],
          [852, 1144, 1553, 429, " - "]]

print("Tabela de distâncias: ")
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(matriz[i][j], end = ' | ')
    print()

print("O quão veloz você vai viajar? (km/h)")
velocidade = int(input("V: "))

tempo_decimal = round(matriz[cidade_1][cidade_2] / velocidade, 2)
tempo_horas = round((0.6 * tempo_decimal) * 100, 0)

if tempo_horas > 60:
    tempo_horas = round(tempo_horas / 60, 2)
    print(f"Você está viajando de {cidades[cidade_1]} até {cidades[cidade_2]}, à uma velocidade de {velocidade}km/h\nO percurso possui {matriz[cidade_1][cidade_2]}km de distância\nSua viagem vai levar cerca de {tempo_horas} horas\n")
else:
    print(f"Você está viajando de {cidades[cidade_1]} até {cidades[cidade_2]}, à uma velocidade de {velocidade}km/h\nO percurso possui {matriz[cidade_1][cidade_2]}km de distância\nSua viagem vai levar cerca de {tempo_horas} minutos\n")
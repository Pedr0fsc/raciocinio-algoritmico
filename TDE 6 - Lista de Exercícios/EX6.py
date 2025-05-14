# A distância rodoviária entre algumas capitais brasileiras está disponível na tabela abaixo. Para
# consultar a distância basta cruzar as cidades origem e destino, ou seja, a distância entre Curitiba e
# São Paulo é de 408 km.
# Construa um programa que inicialize uma matriz contendo as distâncias apresentadas na tabela acima
# e que então informe ao usuário o tempo necessário para percorrer duas cidades por ele fornecidas.

cidades = ["Curitiba (0)", "Florianópolis (1)", "Porto Alegre (2)", "São Paulo (3)", "Rio de Janeiro (4)"]
print(f"{cidades}\n")

cidade_1 = int(input("Diga de qual cidade você vai sair: "))
cidade_2 = int(input("Diga para qual cidade você vai: "))

matriz = [
    [" - ", 310, 716, 408, 852],
    [310, " - ", 470, 705, 1144],
    [716, 470, " - ", 1119, 1553],
    [408, 705, 1119, " - ", 429],
    [852, 1144, 1553, 429, " - "]
]

print("\nTabela de distâncias (em km):")
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        print(f"{matriz[i][j]:>4}", end=' | ')
    print()

velocidade = int(input("\nO quão veloz você vai viajar? (km/h): "))

distancia = matriz[cidade_1][cidade_2]

if isinstance(distancia, str):
    print("Você selecionou a mesma cidade como origem e destino.")
else:
    tempo_horas_decimal = distancia / velocidade
    horas = int(tempo_horas_decimal)
    minutos = round((tempo_horas_decimal - horas) * 60)

    print(f"\nVocê está viajando de {cidades[cidade_1]} até {cidades[cidade_2]}, à uma velocidade de {velocidade}km/h.")
    print(f"O percurso possui {distancia} km de distância.")

    if horas > 0 and minutos > 0:
        print(f"Sua viagem vai levar cerca de {horas} horas e {minutos} minutos.")
    elif horas > 0:
        print(f"Sua viagem vai levar cerca de {horas} horas.")
    else:
        print(f"Sua viagem vai levar cerca de {minutos} minutos.")

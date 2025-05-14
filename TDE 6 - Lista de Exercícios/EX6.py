# A distância rodoviária entre algumas capitais brasileiras está disponível na tabela abaixo. Para
# consultar a distância basta cruzar as cidades origem e destino, ou seja, a distância entre Curitiba e
# São Paulo é de 408 km.
# Construa um programa que inicialize uma matriz contendo as distâncias apresentadas na tabela acima
# e que então informe ao usuário o tempo necessário para percorrer duas cidades por ele fornecidas.

cidades = ["Curitiba (0)", "Florianópolis (1)", "Porto Alegre (2)", "São Paulo (3)", "Rio de Janeiro (4)"]
print(f"{cidades}\n")
cidade_1 = int(input("Diga de qual cidade você vai sair: "))
cidade_2 = int(input("Diga para qual cidade você vai: "))

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
# Considerando a mesma tabela da questão anterior, desenvolva um programa que permita ao usuário
# informar várias cidades em sequência, até inserir um código finalizador. Mostre então as cidades que
# compõem o roteiro fornecido, a distância de cada percurso intermediário e a distância total do roteiro
# fornecido.

cidades = ["Curitiba", "Florianópolis", "Porto Alegre", "São Paulo", "Rio de Janeiro"]

print("Códigos das cidades disponíveis:")
for i, nome in enumerate(cidades):
    print(f"{nome} ({i})")

percurso = []
print("\nDigite os códigos das cidades do seu roteiro. Digite -1 para finalizar.")
while True:
    codigo = int(input("Cidade: "))
    if codigo == -1:
        if len(percurso) < 2:
            print("Informe pelo menos duas cidades.")
            continue
        break
    elif 0 <= codigo < len(cidades):
        percurso.append(codigo)
    else:
        print("Código inválido. Tente novamente.")

matriz = [
    [" - ", 310, 716, 408, 852],
    [310, " - ", 470, 705, 1144],
    [716, 470, " - ", 1119, 1553],
    [408, 705, 1119, " - ", 429],
    [852, 1144, 1553, 429, " - "]
]

velocidade = int(input("\nQual a velocidade média da viagem? (km/h): "))

print("\n--- Roteiro da Viagem ---")
distancia_total = 0
tempo_total_horas = 0

for i in range(len(percurso) - 1):
    origem = percurso[i]
    destino = percurso[i + 1]
    distancia = matriz[origem][destino]

    if isinstance(distancia, str):
        print(f"{cidades[origem]} -> {cidades[destino]}: mesma cidade (0 km, 0 minutos).")
        continue

    tempo_horas = distancia / velocidade
    horas = int(tempo_horas)
    minutos = round((tempo_horas - horas) * 60)

    print(f"{cidades[origem]} -> {cidades[destino]}: {distancia} km, tempo estimado: ", end="")
    if horas > 0 and minutos > 0:
        print(f"{horas} horas e {minutos} minutos.")
    elif horas > 0:
        print(f"{horas} horas.")
    else:
        print(f"{minutos} minutos.")

    distancia_total += distancia
    tempo_total_horas += tempo_horas

horas_total = int(tempo_total_horas)
minutos_total = round((tempo_total_horas - horas_total) * 60)

print("\n--- Resumo da Viagem ---")
print(f"Distância total: {distancia_total} km")
print("Tempo total estimado: ", end="")
if horas_total > 0 and minutos_total > 0:
    print(f"{horas_total} horas e {minutos_total} minutos.")
elif horas_total > 0:
    print(f"{horas_total} horas.")
else:
    print(f"{minutos_total} minutos.")
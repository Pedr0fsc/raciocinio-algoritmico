# Construa um programa que sugira uma aposta de Mega-Sena ou seja, um algoritmo que gera e mostra
# um conjunto de 6 números aleatórios entre [1, 60] sem repetição. Em seguida, obtenha a aposta do
# usuário (sem repetição) e indique quantos acertos ele teve.

import random

mega_sena = sorted(random.sample(range(1, 61), 6))
print(f"\nAposta gerada pela Mega Sena: {mega_sena}")

aposta = set()
print("Digite 6 números de 1 a 60 sem repetições!")

while len(aposta) < 6:
    try:
        numero = int(input(f"Número {len(aposta) + 1}: "))
        if numero < 1 or numero > 60:
            print("Número fora do intervalo!")
        elif numero in aposta:
            print("Número já digitado!")
        else:
            aposta.add(numero)
    except ValueError:
        print("Entrada inválida!")

aposta = sorted(aposta)
print(f"Sua aposta: {aposta}")

acertos = set(aposta) & set(mega_sena)

if len(acertos) > 1 and len(acertos) < 6:
    print(f"Você teve {len(acertos)} acertos com os números: {sorted(acertos)}")
elif len(acertos) == 1:
    print(f"Você teve {len(acertos)} acertos com o número: {sorted(acertos)}")
elif len(acertos) == 6:
    print("Parabéns!!! Você ganhou na Mega Sena!!!")
else:
    print("Você não acertou nenhum número!")
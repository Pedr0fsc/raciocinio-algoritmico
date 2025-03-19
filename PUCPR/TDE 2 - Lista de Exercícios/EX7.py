"""
O IMC (Índice de Massa Corporal) é calculado através da seguinte fórmula:
IMC = massa / altura2
Elabore um algoritmo que leia a massa (em quilogramas) e a altura (em metros) do usuário
e mostre o valor do IMC e se ele está na faixa considerada “normal” segundo o critério
apresentado na tabela da OMS (Organização Mundial de Saúde): 18,5 ≤ IMC< 25. Caso
não esteja, calcule sua massa máxima considerada normal (usando IMC igual a 24,9).
"""

altura = float(input("Insira a sua altura (m): "))
massa = float(input("Insira a sua massa (kg): "))

IMC = massa / altura**2

if(IMC >= 18.5 and IMC < 25):
    print("O seu IMC é de",IMC,"\nVocê está na faixa considerada 'normal'")
else:
    IMC = 24.9
    massa = round(altura**2 * IMC, 3)
    print("Você está fora dos padrões ideais de peso classificados pela OMS\nSua massa máxima considerada 'normal' é igual a",massa,"kg")
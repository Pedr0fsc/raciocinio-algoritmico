"""
O IMC, índice de massa corporal, é calculado através da seguinte fórmula: IMC = massa /
altura2
Elabore um algoritmo que leia a massa (em quilogramas) e a altura (em metros) do
usuário e mostre o valor do IMC e qual sua condição segundo o critério apresentado na
tabela da OMS (Organização Mundial de Saúde):
"""

altura = float(input("Insira a sua altura (m): "))
massa = float(input("Insira a sua massa (kg): "))

IMC = round(massa / altura**2, 1)

def switch(IMC):
    if IMC < 18.5:
        return print("Seu IMC é", IMC, "\nVocê está abaixo do peso")
    elif IMC >= 18.5 and IMC <= 25:
        return print("Seu IMC é", IMC, "\nVocê está no peso normal")
    elif IMC > 25 and IMC <= 30:
        return print("Seu IMC é", IMC, "\nVocê está acima do peso")
    elif IMC > 30:
        return print("Seu IMC é", IMC, "\nObeso")

print(switch(IMC))
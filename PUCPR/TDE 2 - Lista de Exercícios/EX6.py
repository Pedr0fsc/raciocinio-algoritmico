"""
Tendo como dados de entrada a altura (h) e o sexo de uma pessoa (use 1 - masculino e 2 -
feminino) elabore um algoritmo que calcule o peso ideal (p) do usuário utilizando as
seguintes fórmulas:
a. para homens: p = (72.7 * h) - 58
b. para mulheres: p = (62.1 * h) - 44.7
"""

altura = float(input("Insira a sua altura (cm): "))
sexo = int(input("1 - Masculino\n2 - Feminino\nInsira o seu sexo: "))
peso_ideal = float

if(sexo == 1):
    peso_ideal = round((0.75 * altura) - 62.5, 3)
    print("O seu peso ideal é igual a ",peso_ideal,"kg")
elif(sexo == 2):
    peso_ideal = round((0.675 * altura) - 56, 3)
    print("O seu peso ideal é igual a ",peso_ideal,"kg")
else:
    print("Valor indisponível")
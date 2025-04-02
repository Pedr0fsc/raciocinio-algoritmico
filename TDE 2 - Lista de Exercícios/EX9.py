"""
A partir da idade informada de uma pessoa, elabore um algoritmo que informe a sua
classe eleitoral, sabendo que menores de 16 não votam (não votante), que o voto é
obrigatório para adultos entre 18 e 65 anos (eleitor obrigatório) e que o voto é opcional
para eleitores entre 16 e 18, ou maiores de 65 anos (eleitor facultativo).
"""

idade = int(input("Insira a sua idade: "))

if(idade < 16 and idade > 0):
    print("Não votante")
elif(idade >= 18 and idade <= 65):
    print("Eleitor obrigatório")
elif((idade >= 16 and idade < 18) or idade > 65):
    print("Eleitor facultativo")
else:
    print("Valor inadequado! Digite um valor acima de 0")

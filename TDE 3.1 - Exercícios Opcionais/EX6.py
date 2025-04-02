"""
Faça um programa que peça para n pessoas a sua idade, ao final o programa deverá verificar se a
média de idade da turma varia entre 0 e 25, 26 e 60 e maior que 60; e então, dizer se a turma é jovem,
adulta ou idosa, conforme a média calculada.
"""

n = int(input("Digite a quantidade de entrevistados: "))
age_list = []

for n in range(1, n + 1):
    age = int(input("Digite a idade do entrevistado: "))
    age_list.append(age)

media = round(sum(age_list)/len(age_list), 0)

def check_age(media):
    if media >= 0 and media < 26:
        print("A média desse grupo é de: ", media, "\nEles são um grupo JOVEM")
    elif media >= 26 and media < 60:
        print("A média desse grupo é de: ", media, "\nEles são um grupo ADULTO")
    elif media >= 60:
        print("A média desse grupo é de: ", media, "\nEles são um grupo IDOSO")

check_age(media)
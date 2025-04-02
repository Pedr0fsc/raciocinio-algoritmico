"""
Apartir do ano de nascimento informado pelo usuário, elabore um algoritmo que informe
a idade que completará (ou já completou) em 2023. Verifique se ele já pode fazer a carteira
de motorista ou não, informando sua situação.
"""

ano = int(input("Insira seu ano de nascimento: "))
idade_23 = 2023 - ano

if(idade_23 >= 18):
    print("Você já pode tirar a sua CNH!")
else:
    print("Aguarde mais alguns anos...")
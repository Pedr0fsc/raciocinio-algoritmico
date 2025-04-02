"""
Elabore um algoritmo que, dada a idade de um nadador, mostre sua classificação
segundo uma das seguintes categorias:
• 5 até 7 anos: Infantil A;
• 8 até 10 anos: Infantil B;
• 11 até 13 anos: Juvenil A;
• 14 até 17 anos: Juvenil B;
• Maiores de 18 anos: Adulto.
"""

idade = int(input("Insira a sua idade: "))

def switch(idade):
    if idade >= 5 and idade < 8:
        return print("5 até 7 anos: Infantil A")
    elif idade >= 8 and idade < 11:
        return print("8 até 10 anos: Infantil B")
    elif idade >= 11 and idade < 14:
        return print("11 até 13 anos: Juvenil A")
    elif idade >= 14 and idade < 18:
        return print("14 até 17 anos: Juvenil B")
    elif idade >= 18:
        return print("Maiores de 18 anos: Adulto")
    
print(switch(idade))
    
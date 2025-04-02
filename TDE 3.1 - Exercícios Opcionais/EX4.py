"""
Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número
elevado ao segundo número. Não utilize a função de potência da linguagem.
"""

def potencia(base, expoente):
    resultado = 1
    for _ in range(abs(expoente)):
        resultado *= base
    
    if expoente < 0:
        return 1 / resultado
    return resultado

base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

print(f"{base} elevado a {expoente} é igual a {potencia(base, expoente)}")
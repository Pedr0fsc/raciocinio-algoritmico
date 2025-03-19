"""
A partir das informações contidas na tabela abaixo, elabore um algoritmo que leia a
massa em kg de um boxeador e mostre a qual categoria ele pertence. Caso ele não se
encaixe, informe “Categoria inferior a Super-médio”. Lembrando que 1 quilograma =
2,20462262 libras.
"""

peso_kg = float(input("Insira o seu peso em kg: "))
peso_lb = round(peso_kg * 2.20462262, 1)

def switch(peso_lb):
    if peso_lb > 201:
        return print("Massa (lb): ", peso_lb, "lb\nCategoria: Peso-pesado")
    elif peso_lb >= 176 and peso_lb < 201:
        return print("Massa (lb): ", peso_lb, "lb\nCategoria: Cruzador")
    elif peso_lb >= 169 and peso_lb < 176:
        return print("Massa (lb): ", peso_lb, "lb\nCategoria: Meio-pesado")
    elif peso_lb >= 161 and peso_lb < 169:
        return print("Massa (lb): ", peso_lb, "lb\nCategoria: Super-médio")
    else:
        return print("Massa (lb): ", peso_lb, "lb\nCategoria inferior a Super-médio")
    
print(switch(peso_lb))
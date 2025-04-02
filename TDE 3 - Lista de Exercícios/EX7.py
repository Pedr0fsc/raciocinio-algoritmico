"""
Considerando que 1 milha vale exatamente 1.609,344 metros, imprima uma tabela
de conversão de metros (m) para milhas (mi.), de 20 km até 160 km, de 10 em 10
quilômetros.
"""

print("Milhas (mi) | Quilômetros (km) | Metros (m)")
print("-------------------------------------------")

for km in range(20, 161, 10):
    m = km * 1000
    mi = round(m / 1609.344, 2)
    print(f"{mi:>9.2f}mi | {km:>14}km | {m:>9}m")
"""
Supondo que a população de um país A seja da ordem de 80.000 habitantes com uma taxa anual de
crescimento de 3% e que a população de B seja 200.000 habitantes com uma taxa de crescimento de
1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população
do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
"""

pop_A = 80000
pop_B = 200000
tax_A = 0.03
tax_B = 0.015
years = 0

while pop_A < pop_B:
    pop_A = round(pop_A + (pop_A * tax_A), 0)
    pop_B = round(pop_B + (pop_B * tax_B), 0)
    years += 1

print("População inicial de A: 80000  /  População após superar B: ", pop_A)
print("População inicial de B: 200000  /  População após ser superado por A: ", pop_B)
print("Anos até A superar B: ", years, "anos")
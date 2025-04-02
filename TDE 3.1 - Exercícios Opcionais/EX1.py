"""
Ler do teclado uma quantidade de números inteiros a serem lidos e calcular:
a) a soma total entre eles
b) a soma dos que forem pares.
c) a soma dos que forem ímpares
d) a amplitude amostral considerando todos os números lidos (diferença entre o maior e o menor)
"""

num_list = []
even_num_list = []
odd_num_list = []

i = int(input("Informe quantos números você quer digitar: "))

for i in range(1, i + 1):
    num = int(input("Digite um número: "))
    num_list.append(num)
    if num % 2 == 0:
        even_num_list.append(num)
    else:
        odd_num_list.append(num)
    num_list.sort()

num_sum = sum(num_list)

num_amplitude = num_list[-1] - num_list[0]

print("Lista: ", num_list)
print("Números pares: ", even_num_list)
print("Números ímpares: ", odd_num_list)

print("a) Soma dos números da lista: ", num_sum)
print("b) Soma dos números pares: ", sum(even_num_list))
print("c) Soma dos números ímpares: ", sum(odd_num_list))
print("d) Amplitude da lista: ", num_amplitude)

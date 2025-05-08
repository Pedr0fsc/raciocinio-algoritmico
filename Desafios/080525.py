import random

nums = []
nums_par = []

for i in range(1, 11):
    num = random.randint(0, 100)
    nums.append(num)
    if num % 2 == 0:
        nums_par.append(num)
    i += 1

print(f"Lista completa: {nums}\nLista com os números pares: {nums_par}")
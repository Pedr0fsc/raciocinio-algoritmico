# Desenvolva um programa que leia um vetor de 20 posições inteiras e o coloque em ordem crescente,
# utilizando a seguinte estratégia de ordenação:
# • selecione o elemento do vetor de 20 posições que apresenta o menor valor;
# • troque este elemento pelo primeiro;
# • repita estas operações, envolvendo agora apenas os 19 elementos restantes (trocando o de
# menor valor com a segunda posição), depois os 18 elementos (trocando o de menor valor com a
# terceira posição), depois os 17, 16 e assim por diante, até restar um único elemento, o maior
# deles.
# Observação: este método de ordenação é conhecido como “Seleção Direta”.

import random

nums = [random.randint(1, 101) for _ in range(20)]
print(f"Lista dos 20 números a serem lidos: {nums}")

sorted_nums = []

while nums:
    min_num = min(nums)
    sorted_nums.append(min_num)
    nums.remove(min(nums))

print(f"Lista organizada em ordem crescente: {sorted_nums}")

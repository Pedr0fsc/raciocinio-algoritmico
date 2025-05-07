# A Amplitude amostral é uma médida de dispersão, ela é calculada como a diferença entre o valor
# máximo e o valor mínimo de uma amostra. Elabore um programa que leia um vetor de 10 posições
# inteiras e então mostre o valor máximo, o valor mínimo e a amplitude amostral do conjunto
# fornecido.

nums = []

for i in range (10):
    num = int(input("Entre com um número: "))
    nums.append(num)
    i += 1

print(nums)
nums.sort()
print(nums)
amplitude = nums[9] - nums[0]

print("O valor máximo e mínimo dessa lista, respectivamente é", nums[9], "e", nums[0], "\nA amplitude desses valores é igual a", amplitude)
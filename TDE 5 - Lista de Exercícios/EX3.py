# Leia três números do teclado e verificar se o primeiro é maior que a soma dos outros dois.

nums = []

for i in range (0, 3):
    num = int(input("Entre com um número: "))
    nums.append(num)
    i += 1

if nums[0] > (nums[1] + nums[2]):
    print(nums[0], "é maior que a soma de", nums[1], "e", nums[2])
else:
    print(nums[0], "é menor que a soma de", nums[1], "e", nums[2])
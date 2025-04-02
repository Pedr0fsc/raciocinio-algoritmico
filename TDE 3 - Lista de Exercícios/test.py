num_list = []

num = 0

while num != -1:
    num = int(input("Insira um número inteiro: "))
    if num != -1:
        num_list.append(num)

print("A média do seu conjunto de números é: ", sum(num_list) / num_list.__len__())

# Dizemos que um número natural é triangular se ele é produto de três números naturais consecutivos.
# Exemplo: 120 é triangular, pois 4.5.6 = 120. Dado um inteiro não-negativo n, verificar se n é
# triangular.

n = int(input("Digite um número inteiro não negativo: "))
flag = False

i = 1
while i * (i + 1) * (i + 2) <= n:
    if i * (i + 1) * (i + 2) == n:
        flag = True
    else:
        flag = False
    i += 1

if n >= 0:
        if flag == True:
            print(f"{n} é um número triangular.")
        else:
            print(f"{n} não é um número triangular.")

# Esse exercício foi feito sem utilizar uma função e os métodos try e except, diferente desse mesmo exercício da lista 3.1
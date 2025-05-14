m = [[1, 2, 3, 8, 9, 1], 
     [4, 5, 6, 3, 6, 8], 
     [7, 8, 9, 1, 2, 5], 
     [0, 4, 7, 5, 6, 3], 
     [4, 0, 1, 2, 3, 8], 
     [4, 9, 6, 8, 1, 1]]

print("Matriz: ")
for i in range(len(m)):
    for j in range(len(m[0])):
        print(m[i][j], end = ' | ')
    print()

print("Diagonal: ")
for i in range(len(m)):
    for j in range(len(m[0])):
        if i == j:
            print(m[i][j], end = ' | ')
        else:
            print("-", end = ' | ')
    print('')

print("Triângulo Superior: ")
for i in range(len(m)):
    for j in range(len(m[0])):
        if i < j:
            print(m[i][j], end = ' | ')
        else:
            print("-", end = ' | ')
    print('')

print("Triângulo Inferior: ")
for i in range(len(m)):
    for j in range(len(m[0])):
        if i > j:
            print(m[i][j], end = ' | ')
        else:
            print("-", end = ' | ')
    print('')
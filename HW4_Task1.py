# Напишите функцию для транспонирования матрицы
X = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
for r in X:
    print(r)
print()
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for row in range(len(X)):
    for column in range(len(X[0])):
        result[column][row] = X[row][column]
for r in result:
    print(r)
     

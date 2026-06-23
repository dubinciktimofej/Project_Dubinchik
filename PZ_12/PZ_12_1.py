#Вариант 4
# Увеличить все элементы квадратной матрицы,
# не лежащие на главной диагонали, в 2 раза.

n = int(input("Введите размер матрицы n: "))

# Создание матрицы списковым включением
matrix = [[i * n + j + 1 for j in range(n)] for i in range(n)]

print("\nИсходная матрица:")
for row in matrix:
    print(row)

# Преобразование: диагональ не трогаем, остальное умножаем на 2
result = [
    [elem if i == j else elem * 2 for j, elem in enumerate(row)]
    for i, row in enumerate(matrix)
]

print("\nРезультирующая матрица:")
for row in result:
    print(row)
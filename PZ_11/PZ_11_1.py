#Вариант 4. Из последовательности на n целых чисел умножить элементы до n-1 на элемент n
import random

n = int(input("Введите количество элементов: "))
arr = [random.randint(-10, 10) for _ in range(n)]
print("Последовательность: ", arr)

result = list(map(lambda x: x * arr[-1], arr[:-1])) + [arr[-1]]
print("Результат:", result)
#Дан список размера N. Переставить в обратном порядке элементы список,
#расположенные между его минимальным и максимальным элементами, включая
#минимальный и максимальный элементы.
N = int(input("Введите размер списка: "))
A = []

for i in range(N):
    x = int(input(f"Введите A[{i}]: "))
    A.append(x)

print("Исходный список: ", A)


minimum = A.index(min(A))
maximum = A.index(max(A))

left = min(minimum, maximum)
right = max(minimum, maximum)


A[left:right+1] = A[left:right+1] [::-1]
print("Результат: ", A)
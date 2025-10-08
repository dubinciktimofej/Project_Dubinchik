# Дано вещественное число — цена 1 кг конфет. Вывести стоимость 0.1, 0.2, ..., 1 кг
# конфет.
try:
    price = float(input("Введите цену за 1 кг конфет: "))
except ValueError:
    print("Что-то пошло не так. Введите вещественное число!")
a = 1
while a <= 10:
    weight = a / 10
    cost = price * weight
    print(f"{weight} кг -> {cost} руб.")
    a += 1




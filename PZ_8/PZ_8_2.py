#Вариант 4
#Дан словарь с четным кол-вом элементов. Найти суммы значение элементов
#первой и второй половин с исп-ем функции. Результаты вывести на экран

def sum_halves(d):
    values = list(d.values())
    mid = len(values) // 2

    sum1 = sum(values[:mid])  #первая половина словаря
    sum2 = sum(values[mid:])  #вторая половина словаря

    print("Сумма первой половины:", sum1)
    print("Сумма второй половины:", sum2)


<<<<<<< HEAD
slovarik = {"a": 52, "chetverg": 100, "python": 13, "end": 27}
=======
slovarik = {
    "a": 52,
    "chetverg": 100,
    "python": 13,
    "end": 27
}
>>>>>>> 8fb0a923fab7c0a1561bae3d061e4cf9f635b7bd

sum_halves(slovarik)

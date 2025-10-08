# Вариант 4
# 2. Спектр видимого излучения представлен таблице. Составить программу,
# определяющую название цвета в зависимости от введенной длины волны.
try:
    wave_length = int(input("Введите длину волны(нм): "))
except ValueError:
    print("Ошибка ввода: введите целое число в нанометрах.")

if wave_length < 380 or wave_length > 780:
    print("Значение вне видимого спектра.")
elif wave_length <= 449:
    print("Цвет волны фиолетовый.")
elif wave_length <= 479:
    print("Цвет волны синий.")
elif wave_length <= 509:
    print("Цвет волны сине-зелёный.")
elif wave_length <= 549:
    print("Цвет волны зелёный.")
elif wave_length <= 569:
    print("Цвет волны жёлто-зелёный.")
elif wave_length <= 589:
    print("Цвет волны жёлтый.")
elif wave_length <= 629:
    print("Цвет волны оранжевый.")
else: # 630–780
    print("Цвет волны красный.")

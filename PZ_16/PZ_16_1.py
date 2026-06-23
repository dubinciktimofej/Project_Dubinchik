#Создайте класс «Календарь», который имеет атрибуты год, месяц и день. Добавьте
#методы для определения дня недели, проверки на високосный год и определения
#количества дней в месяце

class Calendar:
    """Класс для работы с датами: день недели, високосный год, дней в месяце."""

    # Список дней недели (индекс 0 = воскресенье так работает алгоритм Сакамото)
    DAYS_OF_WEEK = ["Воскресенье", "Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]

    # Количество дней в каждом месяце (индекс 0 заглушка, месяцы идут с 1)
    DAYS_IN_MONTH = [0, 31, 28, 31, 30, 31, 30,
                     31, 31, 30, 31, 30, 31]

    def __init__(self, year, month, day):
        self.year  = year   #год
        self.month = month  #месяц
        self.day   = day    #день

    def is_leap_year(self):
        """Возвращает True, если год високосный."""
        y = self.year
        return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

    def days_in_month(self):
        """Возвращает количество дней в текущем месяце."""
        if self.month == 2 and self.is_leap_year():
            return 29
        return self.DAYS_IN_MONTH[self.month]

    def day_of_week(self):
        """Возвращает название дня недели (алгоритм Томохико Сакамото)."""
        y, m, d = self.year, self.month, self.day
        #Поправочная таблица для каждого месяца
        t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
        #Январь и февраль считаются месяцами предыдущего года
        if m < 3:
            y -= 1
        index = (y + y//4 - y//100 + y//400 + t[m-1] + d) % 7
        return self.DAYS_OF_WEEK[index]

calendar = Calendar(2024, 2, 29)
print(calendar.day_of_week())  
print(calendar.is_leap_year()) 
print(calendar.days_in_month())
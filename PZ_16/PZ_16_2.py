#Создайте класс "Животное", который содержит информацию о виде и возрасте
#животного. Создайте классы "Собака" и "Кошка", которые наследуются от класса
#"Животное" и содержат информацию о породе.

# Базовый класс "Животное"
class Animal:
    """Базовый класс для всех животных"""
    
    def __init__(self, species, age):
        self.species = species  #вид животного
        self.age = age          #возраст животного
    
    def info(self):
        return f"Вид: {self.species}, Возраст: {self.age} лет"


# Класс "Собака", наследуется от Животное
class Dog(Animal):
    """Класс для собак"""
    
    def __init__(self, age, breed):
        super().__init__("Собака", age)  #вызываем конструктор родителя
        self.breed = breed               #порода
    
    def info(self):
        return f"{super().info()}, Порода: {self.breed}"
    
    def sound(self):
        return "Гав!"


#Класс "Кошка", наследуется от Животное
class Cat(Animal):
    """Класс для кошек"""
    
    def __init__(self, age, breed):
        super().__init__("Кошка", age)  #вызываем конструктор родителя
        self.breed = breed              #порода
    
    def info(self):
        return f"{super().info()}, Порода: {self.breed}"
    
    def sound(self):
        return "Мяу!"


#Создаём объекты и проверяем

dog = Dog(age=12, breed="Бульдог")
cat = Cat(age=7,  breed="Сфинкс")

print(dog.info())  #Вид
print(dog.sound()) #Гав!

print(cat.info())  #Вид
print(cat.sound()) #Мяу!
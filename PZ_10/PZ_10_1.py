#Вариант 4
#1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
#последовательность из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:
#Исходные данные:
#Количество элементов:
#Минимальный элемент:
#Элементы, умноженные на первый максимальный элемент:
import random

f = open('input.txt', 'w')
for i in range(5):
    a = random.randint(-10, 10)
    f.write(str(a) + ' ')
f.close()

f = open('input.txt', 'r')
s = f.read()
f.close()

nums = []
for x in s.split():
    nums.append(int(x))

k = len(nums)
mn = min(nums)

mx = max(nums)
first_mx = nums[nums.index(mx)]

f = open('output.txt', 'w', encoding='UTF-8')

f.write('Исходные данные:\n')
f.write(s + '\n')

f.write('Количество элементов: ' + str(k) + '\n')
f.write('Минимальный элемент: ' + str(mn) + '\n')

f.write('Элементы, умноженные на первый максимальный элемент:\n')

for x in nums:
    f.write(str(x * first_mx) + ' ')

f.close()

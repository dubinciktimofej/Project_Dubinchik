text:
        if char.isalpha():
            yield char
#Составить генератор(yield), который выводит из строки только буквы.
def letters_generator(text):
    for char in 
text = "По четвергам рано вставать не надо 184396"
for letter in letters_generator(text):
    print(letter, end="")

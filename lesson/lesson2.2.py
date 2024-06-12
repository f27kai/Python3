"""
list - []
tuple - ()
set - {}
dict - {}
"""

""" 
    ТЕМА: Функция
"""

# def print_hello():
#     print("Hello")
#
# print_hello()


def print_hello(name, surname):
    print(f"Hello {name} {surname}")

print_hello("Musa", "Kimsanbaev")
print_hello("Sanjar", "Muhidinnov")


print(f"Hello Musa Kimsanbaev")



def S(a, b=1000):
    print(a * b)

S(256)
S(256, 5699)
# a = 256
# b = 2589
# S = a * b
# print(S)
#
#
# a = 569
# b = 257
# S = a * b
# print(S)


# def name(name):
#     print(f"Hello {name}")
#
# name("Mile")
# name("Mike")
# name("Baibol")
# name("Sangar")
# name("Islam")
# name("Musa")
#
"""Параметр"""
# def get_square(lenght, width):
#     S = lenght * width
#     print(S)
#
# get_square(256, 214)
# get_square(2565, 2598)


"""Унчукпоо абалы"""

def person(name, nickname="Askarov"):
    print(f"Name: {name}\n"
          f"Nickname: {nickname}")


person("Asan", "!234")
print()
# person(nickname="!234", name="Baibol")




"""Параметрге тибин көрсөтүү"""

# def number(a: int, b: int) -> int:
#     return a + b
#
# num = number(5, 6)
# print(num)

""" Функцияны токтотуп салат """

# def person(name, age):
#     if age > 120 or age < 1:
#         print("Invalid age")
#         return
#     print(f"Name: {name}\n"
#           f"Age: {age}")
#
# person("Asan", 124)


"""Кардардын канча параметрин жазарын билбеген учурда колдонуулучу метод """

# def sum(*numbers):
#     result = 0
#     for number in numbers:
#         result = result + number
#     print(f"Sum: {result}")
#
# sum(5, 6, 256, 589, 85)

""" *args, **kwards """
# def student(*name):
#     return name
#
# a = student("Asan", "Baktybekov")
# print(a)

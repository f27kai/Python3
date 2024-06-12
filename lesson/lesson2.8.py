"""
    ТЕМА: ООП (объектке арналган программоло)
"""

# class Car:
#     marka = "BMW"
#     year = 2011
#     max_speed = 305
#
# bmw = Car()
# bmw.marka = "Mers"
# print(bmw.marka)
# print(bmw.year)
# print(bmw.max_speed)

"""Конструктор"""

# class Car:
#
#     def __init__(self, marka, year, max_speed):
#         self.marka = marka
#         self.year = year
#         self.max_speed = max_speed
#
#     def get_info(self):
#         print(f"Marka: {self.marka}\n"
#               f"Year: {self.year}\n"
#               f"MaxSpeed: {self.max_speed}")
#
# #
# #
# bmw = Car("BMW", "2020", 305)
# bmw.get_info()
#
# print()
# toyota = Car("Toyota", "2024", "240")
# toyota.get_info()
#
# print()
# mersedez = Car("Mersedez", "2019", "350")
# mersedez.get_info()

class Human:
    name = 'Belek'
    surname = 'Asrarov'
    age = 23
    gender = 'male'
    height = '170 cm'

    def say(self):
        print(f"{self.name} is saying.")

    def walk(self):
        print(f"{self.name} is going.")

    def drink(self):
        print(f"{self.name} is drinking.")

belek = Human()
print(belek.name)
print(belek.surname)
print(belek.age)
print(belek.height)
belek.walk()
belek.say()
belek.drink()
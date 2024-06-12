"""
    ТЕМА: ИНКАПСУЛЯЦИЯ
"""

"""Защита"""

# Public
# Protected - защита - _
# Private - __


# class Car:
#
#     def __init__(self, marka, year, max_speed):
#         self.__marka = marka
#         self.__year = year
#         self.__max_speed = max_speed
#
#     def get_marka(self):
#         return self.__marka
#
#     def set_marka(self, newmarka):
#         self.__marka = newmarka
#
#     def get_year(self):
#         return self.__year
#
#     def set_year(self, newyear):
#         self.__year = newyear
#
#     def get_max_speed(self):
#         return self.__max_speed
#
#     def set_max_speed(self, new_maxspeed):
#         self.__max_speed = new_maxspeed
#
#     def get_info(self):
#         print(f"Marka: {self.get_marka()}\n"
#               f"Year: {self.get_year()}\n"
#               f"Max speed: {self.get_max_speed()}")
#
# bmw = Car("BMW", 2022, 305)
# bmw.set_year(2023)
# bmw.get_info()


class Person:

    def __init__(self, name, surname, age, study):
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__study = study

    def get_name(self):
        return self.__name

    def set_name(self, newname):
        self.__name = newname

    def get_surname(self):
        return self.__surname

    def set_surname(self, newsurname):
        self.__surname = newsurname

    def get_age(self):
        return self.__age

    def set_age(self, newage):
        self.__age = newage

    def get_study(self):
        return self.__study

    def set_study(self, newstudy):
        self.__study = newstudy


    def sing(self):
        print(f"{self.__name} is to sing")

    def write(self):
        print(f"{self.__name} is to writing")

    def get_info(self):
        print(f"Name: {self.get_name()}\n"
              f"Surname: {self.get_surname()}\n"
              f"Age: {self.get_age()}\n"
              f"Study: {self.get_study()}")

asan = Person("Asan", "Asanov", "22", "KTMU")
asan.write()
asan.get_info()
"""
    ТЕМА: Мурастоо
"""

class Building:

     def __init__(self, height, width, square, floor):
          self.__height = height
          self.__width = width
          self.__square = square
          self.__floor = floor

     def get_height(self):
          return self.__height

     def set_height(self, height):
          self.__height = height

     def get_width(self):
          return self.__width

     def set_width(self, width):
          self.__width = width

     def get_square(self):
          return self.__square

     def set_square(self, square):
          self.__square = square

     def get_floor(self):
          return self.__floor

     def set_floor(self, floor):
          self.__floor = floor

     def get_info(self):
          print(f"height: {self.get_height()}\n"
                f"width: {self.get_width()}\n"
                f"square: {self.get_square()}\n"
                f"floor: {self.get_floor()}")

class School(Building):

     def __init__(self, height, width, square, floor, gym, library):
          super().__init__(height, width, square, floor)
          self.__gym = gym
          self.__library = library

     def get_gym(self):
          return self.__gym

     def set_gym(self, gym):
          self.__gym = gym

     def get_library(self):
          return self.__library

     def set_library(self, library):
          self.__library = library

     def get_info(self):
          super().get_info()
          print(f"gym: {self.get_gym()}\n"
                f"library: {self.get_library()}")


class House(Building):

     def __init__(self, height, width, square, floor, garage):
          super().__init__(height, width, square, floor)
          self.__garage = garage

     def get_garage(self):
          return self.__garage

     def set_garage(self, garage):
          self.__garage = garage

     def get_info(self):
          super().get_info()
          print(f"garage: {self.get_garage()}")


shool = School("30m", "20m", "600", "5", "yes", "yes")
house = House("10m", "20m", "300", "2", "yes")

shool.get_info()
print()
house.get_info()


"""
     ТЕМА: Полифорфизм
"""

from math import pi

class Shape:
    def __init__(self, lenght):
        self.__lenght = lenght

    def getLenght(self):
        return self.__lenght

    def set_lenght(self, newLenght):
        self.__lenght = newLenght

    def area(self):
        pass

    def fact(self):
        print('Shape!')


class Square(Shape):
    def __init__(self, lenght):
        super().__init__(lenght)

    def area(self):
        print(f"Square areas = {self.getLenght()**2}")

    def fact(self):
        print('Square')


class Circle(Shape):
    def __init__(self, lenght):
        super().__init__(lenght)

    def area(self):
        print(f"Circle areas = {pi*(self.getLenght()/2)**2}")

    def fact(self):
        print('Circle')


square = Square(100)
circle = Circle(10)

square.area()
circle.area()
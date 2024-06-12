"""
    ТЕМА: if elif else
"""

# a = 7
#
# if a == 6:
#     print(6)
# elif a == 7:
#     print(7)
# elif a == 5:
#     print(5)
# elif a == 100:
#     print(100)
# elif a == 8:
#     print(8)
# else:
#     print("Error")


# age = int(input("Сиздин жашыныз канчада? "))
#
# if age < 16:
#     print("Сизге паспорт берилбейт")
# else:
#     print("Сизге паспорт берилет")


# password = "AS1234"
#
# pass1 = input("Enter your password: ")
#
# if pass1 == password:
#     print("Туура")
# else:
#     print("Error")


# x = float(input("x: "))
# option = input("Choose +, -, /, %,  *:   ")
# y = float(input("y: "))
#
# if option == "+":
#     print(x + y)
# elif option == "-":
#     print(x - y)
# elif option == "/":
#     if y == 0:
#         print("Infinity")
#     else:
#         print(x / y)
# elif option == "%":
#       print((x / 100) * y)
# else:
#     print(x * y)


# point = int(input("Алган баллынызды жазыныз: "))
#
# if point < 50:
#     print("Сиз кийинки семестрга өтпөдүнүз")
# elif 50 <= point <= 60:
#     print(2)
# elif 61 <= point <= 75:
#     print(3)
# elif 76 <= point <= 84:
#     print(4)
# else:
#     print(5)

""" 
    ТЕМА: and or not
"""

a = 6

b = a <= 5 and a <= 7
c = a <= 5 or a <= 7
s = not False

print(f"b: {b}\n"
      f"c: {c}\n"
      f"s: {s}")

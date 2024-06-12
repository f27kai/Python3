"""
    ТЕМА: Try except
"""

# try:
#     while True:
#         number = int(input("Bir san jazynyz: "))
#         if number == "Exit":
#             print("Finished ...")
#             break
#         print(number ** 2)
# except:
#     print("Sandy jazynyz")


# try:
#     while True:
#         number = int(input("Bir san jazynyz: "))
#         number_2 = int(input("Bir san jazynyz: "))
#
#         if number == "Exit":
#             print("Finished ...")
#             break
#
#         print(number / number_2)
# except ZeroDivisionError:
#     print("division by zero")
# except ValueError:
#     print("invalid literal for int() with base 10")
#
# print("Except ishtedi")
# print(100 + 100)


try:
    number = int(input("Bir san jazynyz: "))
    print(number ** 2)

except ValueError:
    print("Sandy jazynyz")

else:
    print("!")


# try:
#     number = int(input("Bir san jazynyz: "))
#     print(number ** 2)
#
# except ValueError:
#     print("Sandy jazynyz")
#
# finally:
#     print("!!!")

try:
    number = int(input("bir san jazynyz: "))
    number_2 = int(input("bir san jazynyz: "))
    i = input("Знак (+, -, *, /): ")
    if i == "0":
        a = float(input("a = "))
        b = float(input("b = "))
        if i == "+":
            print("%.2f" % (a + b))
        elif i == "-":
            print("%.2f" % (a - b))
        elif i == "*":
            print("%.2f" % (a * b))
        elif i == "/":
            if b != 0:
                print("%.2f" % (a / b))
            else:
                print("nolgo boly")
except ValueError:
    print("sandy jaz")

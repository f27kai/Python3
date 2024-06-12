"""
    ТЕМА: РЕКУРЦИЯ
"""


# 5! 1 * 2 * 3 * 4 * 5
# def factorial_recursive(n):
#     if n == 1:
#         return n
#     else:
#         return n*factorial_recursive(n-1)
#
# a = int(input("Enter "))
# b = factorial_recursive(a)
# print(b)


"""
    Первый вызов
def factorial_recursive(n):
    if 3 == 1:
        return 3
    else:
        return 3*factorial_recursive(3-1)

a = factorial_recursive(3)
print(a)


     Второй вызов
factorial_recursive(2):
    if 2 == 1:
        return 2
    else:
        return 2*factorial_recursive(2-1)



    Третий вызов
factorial_recursive(1):
    if 1 == 1:
        return 1
    else:
        return 1*factorial_recursive(1-1)
"""

# def person(**name):
#     for key, value in name.items():
#         print(f"{key} = {value}")
#
# person(first_name="Asan", second_name="Baibol")


# my_list = []
# my_list.append(100)
# print(my_list)

"""
max() - сандардын ичинен эн чонун чыгарып берет.
min() - сандардын арасынан эн кичинесин таап берет.
sum() - сандардын суммасын чыгарып берет
"""

i = 0
my_list = [10, 0, 12, 36, 56, 8, 78]

def get_sum(my_list: list):
    counter = 0
    for i in my_list:
        counter += i
    return counter

print(get_sum(my_list))





print(sum(my_list))
# print(max(my_list))
# print(min(my_list))

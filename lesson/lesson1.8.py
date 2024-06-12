"""
    ТЕМА: Эки өлчөмдүү индекс
"""

number = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# print(number[1][1])

# i = 0
# j = 0
#
# while i < len(number):
#     print(number[i][j])
#     i += 1
#     j += 1

# i = 0
# j = 2
#
# while i < len(number):
#     print(number[i][j])
#     i += 1
#     j -= 1

# i = 2
# j = 0
#
# while i < len(number):
#     print(number[i][j])
#     i -= 1
#     j += 1


# i = 0
# j = 0
# while i < len(number):
#     print(number[i][j])
#     i += 1
#     j = (j + 1) % 2

i = 0
j = 0

while i < len(number):
    print(number[i][j])
    if j == 1:
        j -= 2
    i += 1
    j += 1
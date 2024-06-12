# """
#     ТЕМА: цикл While
# """
#
i = 0

while i <= 10:
    j = 0
    while j < 11:
        print(f"{i} * {j} = {i * j}")
        j += 1
    i += 1
    print()
#
#
# while True:
#     point = input("Алган баллынызды жазыныз: ")
#
#     if point == "exit" or point == "выход":
#         print("finished ...")
#         break
#
#     point = int(point)
#
#     if point < 50:
#         print("Сиз кийинки семестрга өтпөдүнүз")
#     elif 50 <= point <= 60:
#         print(2)
#     elif 61 <= point <= 75:
#         print(3)
#     elif 76 <= point <= 84:
#         print(4)
#     else:
#         print(5)
#     print()


# i = 0
# while i < 10:
#     print(i)
#     if i == 2:
#         break
#     i += 1

i = 0

# while i < 11:
#     i += 1
#     if i % 2 == 0:
#         continue
#     print(i)
#
# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)
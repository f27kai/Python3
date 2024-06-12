"""
    ТЕМА: LIST, БЕРИЛИШ СТРУКТУРАЛАРЫ

    БЕРИЛИШ СТРУКТУРАЛАРЫ
    1. LIST --- []
    2. TUPLE (КОРТЕЖ) --- ()
    3. SET --- {}
    4. DIC --- {}
"""

# name = "Asan"
# name1 = "Саидмырза"
# name2 = "Uzair"
# print(name, name1, name2)

name = ["Саидмырза", "Uzair", "Каныкей", "Ислам", "Сагынбек", "Байбол"]
# print(name)

"""INDEX"""
# print(name[4][2])

"""ADD"""
# name.append("Bakyt")
# name.extend(["Aygerim", "Marsel", "Manas", "Argen", "Marat"])
# name.insert(1, "Merim")
# name.insert(3, "Balasagun")
# print(name)

"""UPDATE"""
# name[0] = "Шрек"
# print(name)


"""DELETE"""
# name.remove("Asan")
# print(name)
# name.pop(2)
# del name[1]
# print(name)


# name = name.count("Asan")
# print(name.index("Сагынбек"))

# my_list = [7, 5, 8, 2, 11, 1, 14]
# print(my_list)
# my_list.reverse()
# print(f"my_list.reverse() --- {my_list}")
# my_list.sort()
# print(f"my_list.sort() --- {my_list}")
# my_list.sort(reverse=True)
# print(f"my_list.sort(reverse=True) --- {my_list}")

# name.clear()
# print(name)


# my_list = []
# jup = []
# tak = []
#
# for i in range(101):
#     my_list.append(i)
#     if i % 2 == 0:
#         jup.append(i)
#     else:
#         tak.append(i)
#
# print(f"Бардык сандар: {my_list}")
# print(f"Жуп сандар: {jup}")
# print(f"Так сандар: {tak}")


madrid = ["Uzair", "Islam", "Baybol"]
shumkar = ["Sagynbek", "Kanikey", "Saidmyrza"]

madrid.extend(["Mbappe", "Sadyr", "Kamchy"])
shumkar.extend(["Maikl", "Piter", "Jony"])


madrid.pop(1)
shumkar.remove("Maikl")


madrid[3] = "Nick"
shumkar[3] = "Rekorda Rosha"

print(f"Madrid comand: {madrid}")
print(f"Shumkar comand: {shumkar}")





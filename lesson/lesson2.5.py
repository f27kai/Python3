"""
    ТЕМА: TUPLE, DICT, SET
"""

"""LIST"""

# my_list = ["Musa", "Islam", "Sanjar", "Baibol"]
# print(my_list[1])

# my_list[2] = "Bakyt"
# print(my_list)

# my_list.extend(["Sagynbek", "Uzair"])
# print(my_list)

# my_list.sort()
# my_list.sort(reverse=True)
# print(f"my_list.sort(reverse=True): {my_list}")
# my_list.reverse()
# print(f"my_list.reverse(): {my_list}")

# my_list.pop()
# my_list.remove()
# del my_list[]

"""TUPLE"""
# my_tuple = ("Musa", "Islam", "Sanjar", "Baibol")
# print(my_tuple[:2])
# number = 5,

"""SET"""
# plov = {"et", "sabiz", "chesnok", "guruch", "piyaz"}
# beshbarmak = {"et", "kamyr", "piyaz"}

# print(plov.union(beshbarmak))
# print(plov.difference(beshbarmak))
# print(plov.intersection(beshbarmak))
# print(plov.symmetric_difference(beshbarmak))

"""Dict"""
# kyrgystan = {
#     "capital": "Bishkek",
#     "region": 7,
#     "population_size": "8 milion",
#     "Independence_Day": "1991 year, 31 august"
# }

"""Функция"""
# def get_square(lenght: int, width=300) -> int:
#     square = lenght * width
#     return square
#
# S = get_square(400, 40)
# print(S)


"""lambda --- функция"""
# def upper_words(function, words):
#     for i in words:
#         print(function(i))
#
# upper_words(lambda word: word.upper(),["musa", 'sanjar', 'baibol', "islam"])
#

# name_filter = tuple(filter(lambda name: len(name) > 4, ["musa", 'sanjar', 'baibol', "islam"]))
# print(name_filter)
#
# name_map = list(map(lambda word: word.upper(), ["musa", 'sanjar', 'baibol', "islam"]))
# print(name_map)
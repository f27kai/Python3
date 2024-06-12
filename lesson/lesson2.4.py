"""
    ТЕМА: Функция lambda
"""

def letter(world: str):
    return world.title()

# name = "asan"
# print(letter(name))

def upper_world(function, words):
    return [function(i) for i in words]


my_list = ["asAn",'sanjar', 'musa', "saidmyrza", 'kanikei', 'nurmuhammed']
#
# a = upper_world(letter, my_list)
# print(a)

# upper_world(lambda word: word.title(), ["asAn",'sanjar', 'musa'])


# a = list(filter(lambda world: len(world) > 5, ["asAn",'sanjar', 'musa', "saidmyrza", 'kanikei', 'nurmuhammed']))
# print(a)

# b = list(map(lambda world: world.upper(), my_list))
# print(b)


number = [1, 0, 23, 56, 89, 44, 2, 36, 22, 38]

print(tuple(filter(lambda number: number % 2 == 0, number)))
print(tuple(map(lambda number: round(number / 2, 2) , number)))

for i in my_list:
    print(i, len(i))
"""
    Текст менен иштеле турган методдор

    пер.isdigit() - жазылган элементтин баары санбы ошону текшерип берет.
    пер.isalpha() - жазылган элементтин баары тамгабы ошону чыгарат.
    пер.isalnum() - сан тамга аралышпы ошону текшерип берет
    пер.islower() - бардык тамга кичине болсо True деп чыгарат, бир эле тамга чон болсо False деп чыгарат
    пер.isupper() - бардык тамга чон болсо True деп чыгарат, бир эле тамга кичине болсо False деп чыгарып берет
    пер.istitle() -биринчи тамга чонбу же кичинеби текшерет
    пер.lower() - тамгалардын баарын кичине кылып салат
    пер.upper() - тамгалардын баарын чон кылып салат
    пер.startwith(Hi) - баштапкы тамгаларды текшерсе болот
    пер.endswith(12) - акыркы соз кайсыл тамга менен бутконун текшерет
    пер.split() -  текстти листке айландырват
    пер.replace(баштапкы маани, кайсыл созго озгортобуз) - Созду озгортуп берет

    пер - бул переменный
"""

# a = "126A"
# print(a.isdigit())

# b = "Asan12"
# print(b.isalpha())
#
# c = "Asan27"
# print(c.isalnum())

# cd = "saNa"
# print(cd.islower())

# cd = "AsaN"
# print(cd.lower())
# print(cd.istitle())
# print(cd.isupper())

# name = input("Atynyz: ")
# print(name.lower())
# print(name.upper())

# NumText = "Hi 123 Sanjar"
# NumText = "Sanjar"
# print(NumText.split())


# print(f"replaceке чейин: {NumText}")
# print("replaceке колдонгондон кийин: ", NumText.replace("123", "Asan"))

# text = "Hello123"
# print(text.startswith("He"))
# print(text.endswith("423"))

"""Срезы [start:stop:step]"""
# range(1,100)
# name = ["Саидмырза", "Uzair", "Каныкей", "Ислам", "Сагынбек", "Байбол"]
# print(f"Do: {name}")
# print(f"Posle: {name[1:5]}")
# print(f"Posle: {name[:5:2]}")
# print(f"Posle: {name[:3]}")
# print(f"Posle: {name[:-3]}")

# while True:
#     world = input("Enter your text: ")
#
#     if world == "Exit":
#         print("Finished ... ")
#         break
#
#     world = world.lower()
#     print(world.split())

number = input("Sandy jazynyz: ")
print(number[::-1])
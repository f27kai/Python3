def print_hello(name, surname):
    print(f"Hello {name} {surname}")

def S(a, b=1000):
    print(a * b)

def your_age():
    age = int(input("Сиздин жашыныз канчада? "))

    if age < 16:
        print("Сизге паспорт берилбейт")
    else:
        print("Сизге паспорт берилет")
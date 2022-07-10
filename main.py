import helper as h
import random
import colorama


def incorrect_input():
    print(colorama.Fore.RED + "Неправильный номер, попробуйте ещё раз")


def info():
    print("Выберете генератор:\n1) Генератор персонажей\n2) Генератор названий\n3) Генератор городов")
    print(colorama.Fore.RED + "Введите quit чтобы выйти\n" +
          colorama.Fore.YELLOW + "Введите list чтобы показать это сообщение ещё раз")


def create_character():
    data = dict()
    data["class"] = random.choice(h.classes)
    data["race"] = random.choice(h.races)
    data["gender"] = "Мужской" if random.randint(0, 1) == 0 else "Женский"
    if data["gender"] == "Женский":
        data["name"] = random.choice(h.female_names)
    else:
        data["name"] = random.choice(h.male_names)
    data["surname"] = random.choice(h.surnames)
    data["level"] = random.randint(1, 20)
    return data


def create_name():
    name = ""
    for _ in range(1, 4):
        name += random.choice(h.strange_names)
    name = name.title()
    return name


colorama.init(autoreset=True)
info()
while True:
    try:
        n = input(">")
        if n == "1":
            char = create_character()
            print(f"Имя: {char['name']} {char['surname']}")
            print(f"Пол: {char['gender']}")
            print(f"Расса: {char['race']}")
            print(f"Класс: {char['class']}")
            print(f"Уровень: {char['level']}")
        elif n == "2":
            print(create_name())
        elif n == "3":
            creator = create_character()
            town_name = create_name()
            print(creator)
            print(town_name)
        elif n in ('q', 'quit', 'e', 'exit'):
            break
        elif n in ('list', 'l', 'spis', 's', 'info', 'i'):
            info()
        else:
            incorrect_input()
    except ValueError:
        incorrect_input()

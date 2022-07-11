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


def create_town():
    creator = create_character()
    town_name = create_name()
    age = random.randint(6, 1000)
    peoples = round(age, -1) * random.choice((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100))  # FIXME stupid way
    kids = peoples // random.randint(5, 50)
    living_buildings = random.randint(peoples // 2, peoples)
    taverns = random.randint()


colorama.init(autoreset=True)
info()
while True:
    try:
        n = input(">")
        if n == "1":
            char = create_character()
            print(f"Имя: {colorama.Fore.GREEN}{char['name']} {char['surname']}")
            print(f"Пол: {colorama.Fore.GREEN}{char['gender']}")
            print(f"Расса: {colorama.Fore.GREEN}{char['race']}")
            print(f"Класс: {colorama.Fore.GREEN}{char['class']}")
            print(f"Уровень: {colorama.Fore.GREEN}{char['level']}")
        elif n == "2":
            print(create_name())
        elif n == "3":


            print(f"Город {colorama.Fore.GREEN}{town_name}")
            print(f"Был основан {colorama.Fore.GREEN}{age}{colorama.Fore.RESET} годами ранее")
            print(f"Основатель - {colorama.Fore.YELLOW}{random.choice(h.titles)} {colorama.Fore.GREEN}{creator['name']} {creator['surname']}")
            print("Здания:")
            print(f"Жилые здания - {random.randint(0, age * 2)}")
            print(f"Таверна - ")
        elif n in ('q', 'quit', 'e', 'exit'):
            break
        elif n in ('list', 'l', 'spis', 's', 'info', 'i'):
            info()
        else:
            incorrect_input()
    except ValueError:
        incorrect_input()

import random

import colorama

import ruhelper as h


def incorrect_input():
    print(colorama.Fore.RED + "Неправильный номер, попробуйте ещё раз")


def info():
    print("Выберете генератор:\n1) Генератор персонажей\n2) Генератор названий\n3) Генератор городов")
    print(colorama.Fore.RED + "Введите quit чтобы выйти\n" +
          colorama.Fore.YELLOW + "Введите list чтобы показать это сообщение ещё раз")


class Humanoid:
    def __init__(self, *, titular=False):
        self.race = random.choice(h.races)
        self.gender = "Мужской" if random.randint(0, 1) == 0 else "Женский"
        self.name = random.choice(h.female_names if self.gender == "Женский" else h.male_names)
        self.surname = random.choice(h.surnames)
        self.title = random.choice(h.female_titles if self.gender == "Женский" else h.male_titles) if titular else ""
        self.full_name = self.title + " " + self.name + " " + self.surname if titular else self.name + " " + self.surname  # fixme?

    def __str__(self):
        return f"{self.race} {self.full_name}"

    def print_full_info(self):
        print(f"Имя: {colorama.Fore.GREEN}{self.full_name}")
        print(f"Пол: {colorama.Fore.GREEN}{self.gender}")
        print(f"Расса: {colorama.Fore.GREEN}{self.race}")


class NPC(Humanoid):
    def __init__(self, *, titular=False):
        super().__init__(titular)
        self.Class = random.choice(h.classes)
        self.level = random.randint(1, 20)

    def __str__(self):
        return f"{self.race} {self.Class} {self.level} {self.full_name}"

    def print_full_info(self):
        super().print_full_info()
        print(f"Класс: {colorama.Fore.GREEN}{self.Class}")
        print(f"Уровень: {colorama.Fore.GREEN}{self.level}")


class Building:
    def __init_subclass__(cls, **kwargs):
        cls.age: int = None
        cls.type: str = None
        cls.name: str = None
        cls.material: str | list = None
        cls.creator: NPC = None


class Name:
    def __init__(self, length=4):
        name = ""
        for _ in range(length):
            name += random.choice(h.strange_names)
        self.name = name.title()

    def __str__(self):
        return self.name


class Town:
    def __init__(self):
        self.creator = NPC(titular=False if random.randint(0, 1000) == 0 else True)
        self.town_name = Name()
        self.age = random.randint(6, 5000)
        self.peoples = round(self.age, -1) * random.choice(
            (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100))  # fixme stupid way
        self.kids = self.peoples // random.randint(5, 50)
        self.living_buildings = random.randint(self.peoples // 3, self.peoples)

        if self.age < 100:
            if random.randint(0, 100) <= 5:
                self.taverns = [Tavern(self)]
            else:
                self.taverns = list()
        else:
            self.taverns = list([Tavern(self) for _ in range(random.randint(1, self.age // 100))])

        if self.age < 200:
            self.religion_bildings = [ReligionBuilding()]
        else:
            self.religion_bildings = list([ReligionBuilding() for _ in range(random.randint(1, self.age // 100))])


class Tavern(Building):
    def __init__(self, in_town: Town):
        self.age = random.randint(0, in_town.age)
        self.type = "Таверна"
        self.name = Name().name
        self.material = random.choice(h.materials)
        self.creator = NPC() if in_town.age - self.age > 40 and random.randint(0, 1) == 0 else in_town.creator
        self.barman = NPC()

    def __str__(self):
        return self.name


class ReligionBuilding(Building):
    pass


if __name__ == "__main__":
    colorama.init(autoreset=True)
    info()
    last_function_called = None
    while True:
        try:
            n = input(">")
            if n == "1":
                NPC().print_full_info()
            elif n == "2":
                print(Name())
            elif n == "3":
                town = Town()
                print(f"Город: {town.town_name}")
                print(f"Основатель: {town.creator}")
                print(f"Основан {town.age} лет назад")
                print(f"Население: {town.peoples}, из них дети: {town.kids}")
                print(f"Жилые здания: {town.living_buildings}, таверны: {len(town.taverns)}")
                print(f"Храмов, мечетей и других религиозных построек: {len(town.religion_bildings)}")
            elif n in ('q', 'quit', 'e', 'exit'):
                break
            elif n in ('list', 'l', 'spis', 's'):
                info()
            elif n in ('info', 'i'):
                pass
            else:
                incorrect_input()
        except ValueError:
            incorrect_input()

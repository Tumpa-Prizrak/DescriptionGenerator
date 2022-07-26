from operator import le
import random

import colorama
import requests

import rulang as h

def colorate(phraze: dict):
    """{"phraze": "color"}"""
    out = ""
    for i in phraze.keys():
        if phraze[i] is None:
            out += i
        else:
            out += phraze[i] + i
    print(out)

class GeneratorUrl:
    def __init__(self):
        self.__url_name = "https://www.kassoon.com/dnd/name-generator/{}-{}-English"
    
    def generate_name(self, gender: str, race: str):
        requests.get(self.__url_name.format(h.to_requests['gender'][gender], h.to_requests['race'][race]), timeout=1).content.decode().split("<br/>")[1]

class Name:
    def __init__(self, length=4):
        name = ""
        for _ in range(length):
            name += random.choice(h.strange_names)
        self.name = name.title()

    def __str__(self):
        return self.name


class ABC:
    def __init__(self, *, age: int = None, name: str = None):
        self.age: int = age
        self.name: str = name

    def __str__(self):
        return self.name

    def print_full_info(self):
        print(f"{self.name=}\n{self.age=}")


# ----------------------------------------------------------------------------------------------------------------------


class Building(ABC):
    def __init_subclass__(cls, **kwargs):
        super().__init__(cls)
        cls.type: str = None
        cls.material: str | list = None
        cls.creator: Humanoid = None
    
    def join(self):
        self.visitors = random.randint(0, self.__town.peoples // 100 + 1)


class Humanoid(ABC):
    def __init__(self, *, titular=False):
        self.gender = "Мужской" if random.randint(0, 1) == 0 else "Женский"
        super().__init__(name=random.choice(h.female_names if self.gender == "Женский" else h.male_names),
                         age=random.randint(16, 80))
        self.race = random.choice(h.races)
        self.surname = random.choice(h.surnames)
        try:
            self.name, self.surname = GeneratorUrl().generate_name(self.gender, self.race)
        except requests.ConnectionError:
            pass
        self.title = random.choice(h.female_titles if self.gender == "Женский" else h.male_titles) if titular else ""
        self.full_name = self.title + " " + self.name + " " + self.surname if titular else self.name + " " + self.surname  # FIXME:?

    def __str__(self):
        return f"{self.race} {self.full_name}"

    def print_full_info(self):
        print(f"Имя: {colorama.Fore.GREEN}{self.full_name}")
        if self.title != "":
            print(f"Титул: {colorama.Fore.GREEN}{self.title}")
        print(f"Расса: {colorama.Fore.GREEN}{self.race}")
        print(f"Пол: {colorama.Fore.GREEN}{self.gender}")
        print(f"Возраст {colorama.Fore.GREEN}{self.age}{colorama.Fore.RESET} человеческих лет")


class Town(ABC):
    def __init__(self):
        super().__init__(age=random.randint(1, 1000), name=Name().name)
        self.creator = Humanoid(titular=False if random.randint(0, 1000) == 0 else True)
        self.peoples = (round(self.age, -1) * random.choice(range(1, 3))) // 2  # FIXME: stupid way
        self.kids = self.peoples // random.randint(15, 50)
        self.living_buildings = random.randint(self.peoples // 3, self.peoples)
        self.taverns = list([Tavern(self) for _ in range(random.randint(0, self.peoples // 100))])
        self.religion_bildings = list([ReligionBuilding(self) for _ in range(random.randint(0, self.peoples // 100))])
        # TODO: play with this values

    def print_full_info(self):
        print(f"Город: {self.name}")
        print(f"Основатель: {self.creator}")
        print(f"Основан {self.age} лет назад")
        print(f"Население: {self.peoples}, из них дети: {self.kids}")
        print(f"Жилые здания: {self.living_buildings}, таверны: {len(self.taverns)}")
        print(f"Храмов, мечетей и других религиозных построек: {len(self.religion_bildings)}")
    
    def join(self):
        while True:
            colorate({"Религиозные здания:": colorama.Fore.YELLOW})
            for i in range(len(self.religion_bildings)):
                print(f"R{i}) {self.religion_bildings[i].type} {self.religion_bildings[i].name}")
            colorate({"Таверны:": colorama.Fore.YELLOW})
            for i in range(len(self.taverns)):
                print(f"T{i}) {self.taverns[i].type} {self.taverns[i].name}")
            c = input("Введите код здания: ").upper()
            if c.startswith("R"):
                #try:
                self.religion_bildings[int(c[1:])].join()
                break
                #except IndexError:
                #    colorate({"Неправильный ввод": colorama.Fore.RED})
            elif c.startswith("T"):
                try:
                    self.taverns[int(c[1:])].join()
                    break
                except IndexError:
                    colorate({"Неправильный ввод": colorama.Fore.RED})
            else:
                colorate({"Неправильный ввод": colorama.Fore.RED})
            


# ----------------------------------------------------------------------------------------------------------------------


class NPC(Humanoid):
    def __init__(self, *, titular=False):
        super().__init__(titular=titular)
        self.Class = random.choice(h.classes)
        self.level = random.randint(1, 20)

    def __str__(self):
        return f"{self.race} {self.Class} {self.level} {self.full_name}"

    def print_full_info(self):
        super().print_full_info()
        print(f"Класс: {colorama.Fore.GREEN}{self.Class}")
        print(f"Уровень: {colorama.Fore.GREEN}{self.level}")


class Tavern(Building):
    def __init__(self, in_town: Town):
        self.__town = in_town
        super().__init__(age=random.randint(0, self.__town.age), name=Name().name)
        self.material = random.choice(h.materials)
        self.creator = Humanoid() if in_town.age - self.age > 40 and random.randint(0, 1) == 0 else in_town.creator
        self.barman = None
        self.barman_only_one = bool(random.randint(0, 1))
        if self.barman_only_one:
            self.barman = Humanoid()
        self.visitors = 0
        self.monthly_additions = (self.__town.peoples // 100 + 1) * random.randint(1, 10)

    def join(self):
        super().join()
        if not self.barman_only_one:
            self.barman = Humanoid()
        print(f"Вы входите в таверну {self.name} и видите {len(self.visitors)} человек и бармена {self.barman}")


class ReligionBuilding(Building):
    def __init__(self, in_town: Town):
        self.__town = in_town
        super().__init__(age=random.randint(0, self.__town.age))
        self.material = random.choice(h.materials)
        self.creator = Humanoid() if in_town.age - self.age > 40 and random.randint(0, 1) == 0 else in_town.creator
        self.main_prienst = Humanoid()
        self.visitors = list()
    
    def join(self):
        super().join()
        print(f"Вы входите в {self.name} и видите {len(self.visitors)} человек" + "и видите епископа" if random.randint(0, 1) == 1 else ", но не видите епископа")

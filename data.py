from abc import ABC, abstractclassmethod
from typing import Dict, Literal
from random import choice


class Race(ABC):
    gender: Literal["female", "male"]
    data: dict

    @abstractclassmethod
    def __init__(self, gender: Literal["female", "male"]) -> None:
        ...

    @abstractclassmethod
    def __str__(self) -> str:
        ...
    
    @abstractclassmethod
    def to_json(self) -> dict:
        ...


class Dwarf(Race):
    data = {
        "first_name": {
            "male": ['Adrik', 'Alberich', 'Baern', 'Barendd', 'Brottor', 'Bruenor', 'Dain', 'Darrak', 
                     'Delg', 'Eberk', 'Einkil', 'Fargrim', 'Flint', 'Gardain', 'Harbek', 'Kildrak', 
                     'Morgran', 'Orsik', 'Oskar', 'Rangrim', 'Rurik', 'Taklinn', 'Thoradin', 'Thorin', 
                     'Tordek', 'Traubon', 'Travok', 'Ulfgar', 'Veit', 'Vondal'],
            "female": ['Amber', 'Artin', 'Audhild', 'Bardryn', 'Dagnal', 'Diesa', 'Eldeth', 'Falkrunn', 
                       'Finellen', 'Gunnloda', 'Gurdis', 'Helja', 'Hlin', 'Kathra', 'Kristryd', 'Ilde', 
                       'Liftrasa', 'Mardred', 'Riswynn', 'Sannl', 'Torbera', 'Torgga', 'Vistra']
        },
        "clan": ['Balderk', 'Battlehammer', 'Brawnanvil', 'Dankil', 'Fireforge', 'Frostbeard', 'Gorunn', 
                 'Holderhek', 'Ironfist', 'Loderr', 'Lutgehr', 'Rumnaheim', 'Strakeln', 'Torunn', 
                 'Ungart'],
        "nickname": ['Badger', 'Barefoot', 'Two-lock', 'Kolotushka', 'Ku', 'Nim', 'Peploserd', 
                     'Beerhawk', 'Cloak', 'Pok', 'Seablossom', 'Stumbledac', 'Fnipper']
    }

    def __init__(self, gender: Literal["female", "male"]) -> None:
        self.gender = gender
        self.first_name = self.get_first_name()
        self.clan = self.get_clan()
        self.nickname = self.get_nickname()
    
    def get_first_name(self) -> str:
        return choice(self.data.get("first_name").get(self.gender))

    def get_clan(self) -> str:
        return choice(self.data.get("clan"))
    
    def get_nickname(self) -> str:
        return choice(self.data.get("nickname"))

    def __str__(self) -> str:
        return f"{self.first_name} {self.clan} ({self.nickname})"
    
    def to_json(self) -> dict:
        return {
            "gender": self.gender,
            "first_name": self.first_name,
            "clan": self.clan,
            "nickname": self.nickname,
            "printable": str(self)
        }


class Elf(Race):
    data = {
        "first_name": {
            "child": ['Ara', 'Bryn', 'Del', 'Eryn', 'Faen', 'Innil', 'Lael', 'Mella', 'Naill', 
                      'Naeris', 'Phann', 'Rael', 'Rinn', 'Sai', 'Syllin', 'Thia', 'Vall'],
            "adult": {
                "male": ['Adran', 'Aelar', 'Aramil', 'Arannis', 'Aust', 'Beiro', 'Berrian', 'Carric', 
                         'Enialis', 'Erdan', 'Erevan', 'Galinndan', 'Hadarai', 'Heian', 'Himo', 
                         'Immeral', 'Ivellios', 'Laucian', 'Mindartis', 'Paelias', 'Peren', 'Quarion', 
                         'Riardon', 'Rolen', 'Soveliss', 'Thamior', 'Tharivol', 'Theren', 'Varis'],
                "female": ['Adrie', 'Althaea', 'Anastrianna', 'Andraste', 'Antinua', 'Bethrynna', 
                           'Birel', 'Caelynn', 'Drusilia', 'Enna', 'Felosial', 'Ielenia', 'Jelenneth', 
                           'Keyleth', 'Leshanna', 'Lia', 'Meriele', 'Mialee', 'Naivara', 'Quelenna', 
                           'Quillathe', 'Sariel', 'Shanairra', 'Shava', 'Silaqui', 'Theirastra', 'Thia', 
                           'Vadania', 'Valanthe', 'Xanaphia']
            }
        },
        "last_name": ['Amakiir (Gemflower)', 'Amastacia (Starflower)', 'Galanodel (Moonwhisper)', 
                      'Holimion (Diamonddew)', 'Ilphelkiir (Gemblossom)', 'Liadon (Silverfrond)', 
                      'Meliamne (Oakenheel)', 'Naïlo (Nightbreeze)', 'Siannodel (Moonbrook)', 
                      'Xiloscient (Goldpetal)']
    }

    def __init__(self, gender: Literal["female", "male"]) -> None:
        self.gender = gender
        self.first_name = self.generate_first_name()
        self.last_name = self.generate_last_name()
    
    def generate_first_name(self) -> str:
        return choice(self.data.get("first_name").get("adult").get(self.gender))

    def generate_last_name(self) -> str:
        return choice(self.data.get("last_name"))
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    def to_json(self) -> dict:
        return {
            "gender": self.gender,
            "first_name": self.first_name,
            "last_name": self.last_name
        }


races: Dict[str, Race] = {  # TODO finish
    "dwarf": Dwarf,
    "elf": Elf
}
races_list = ["gnome", "dwarf", "dragonborn", "half-orc", "halfling", 
              "half-elf", "tiefling", "human", "elf"]

from data.races.ABC import Race
from typing import Literal
from random import choice

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

class Dwarf(Race):
    def __init__(self, gender: Literal["female", "male"]) -> None:
        self.gender = gender
        self.first_name = self.get_first_name()
        self.clan = self.get_clan()
        self.nickname = self.get_nickname()
    
    def get_first_name(self) -> str:
        return choice(data.get("first_name").get(self.gender))

    def get_clan(self) -> str:
        return choice(data.get("clan"))
    
    def get_nickname(self) -> str:
        return choice(data.get("nickname"))

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
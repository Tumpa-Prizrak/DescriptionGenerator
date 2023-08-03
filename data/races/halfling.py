from data.races.ABC import Race
from typing import Literal
from random import choice


data = {
    "first_name": {
        "male": ['Alton', 'Ander', 'Cade', 'Corrin', 'Eldon', 'Errich', 'Finnan', 'Garret', 
                    'Lindal', 'Lyle', 'Merric', 'Milo', 'Osborn', 'Perrin', 'Reed', 'Roscoe', 
                    'Wellby'],
        "female": ['Andry', 'Bree', 'Callie', 'Cora', 'Euphemia', 'Jillian', 'Kithri', 'Lavinia', 
                    'Lidda', 'Merla', 'Nedda', 'Paela', 'Portia', 'Seraphina', 'Shaena', 'Trym', 
                    'Vani', 'Verna']
    },
    "last_name": ['Brushgather', 'Goodbarrel', 'Greenbottle', 'High-hill', 'Hilltopple', 
                    'Leagallow', 'Tealeaf', 'Thorngage', 'Tosscobble', 'Underbough']
}


class Halfling(Race):
    def __init__(self, gender: Literal["female", "male"]) -> None:
        self.gender = gender
        self.first_name = self.generate_first_name()
        self.last_name = self.generate_last_name()
    
    def generate_first_name(self) -> str:
        return choice(self.data.get("first_name").get(self.gender))

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
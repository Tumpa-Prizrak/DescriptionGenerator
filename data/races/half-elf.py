from data.races.ABC import Race
from typing import Literal
from random import choice, randint
from data.races.elf import data as elf_data
from data.races.human import data as human_data

class HalfElf(Race):
    def __init__(self, gender: Literal["female", "male"]) -> None:
        self.gender = gender
        self.is_elf: bool = bool(randint(0, 1))
        self.first_name = self.generate_first_name()
        self.last_name = self.generate_last_name()
    
    

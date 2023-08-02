from pydantic import BaseModel
from typing import Literal


class Race(BaseModel):
    race: Literal["gnome", "dwarf", "dragonborn", "half-orc", "halfling", 
                  "half-elf", "tiefling", "human", "elf"] | None = None
    gender: Literal["female", "male"] | None = None

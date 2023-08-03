from .ABC import Race
from .dwarf import Dwarf

races: dict[str, Race] = {  # TODO finish
    "dwarf": Dwarf,
    # "elf": Elf,
    # "halfling": Halfling,
    # "human": Human,
}
races_list = ["dwarf"] #"gnome", "dragonborn", "half-orc", "halfling", 
              #"half-elf", "tiefling", "human", "elf"]

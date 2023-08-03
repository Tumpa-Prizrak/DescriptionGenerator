from data.races.ABC import Race
from typing import Literal
from random import choice


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


class Elf(Race):
    def __init__(self, gender: Literal["female", "male"]) -> None:
        self.gender = gender
        self.first_name = self.generate_first_name()
        self.last_name = self.generate_last_name()
    
    def generate_first_name(self) -> str:
        return choice(data.get("first_name").get("adult").get(self.gender))

    def generate_last_name(self) -> str:
        return choice(data.get("last_name"))
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    def to_json(self) -> dict:
        return {
            "gender": self.gender,
            "first_name": self.first_name,
            "last_name": self.last_name
        }
from data.races.ABC import Race
from typing import Literal
from random import choice


class Human(Race):
    data = {
        'Calishite': {
            "first_name": {
                "male": ['Aseir', 'Bardeid', 'Haseid', 'Khemed', 'Mehmen', 'Sudeiman', 'Zasheir'],
                "female": ['Basha', 'Dumein', 'Jassan', 'Khalid', 'Mostana', 'Pashar', 'Rein']
            },
            "last_name": ['Atala', 'Ceidil', 'Hama', 'Jasmal', 'Meilil', 'Seipora', 'Yasheira', 
                          'Zasheida']
        },
        'Chondathan': {
            "first_name": {
                "male": ['Darvin', 'Dorn', 'Evendur', 'Gorstag', 'Grim', 'Helm', 'Malark', 'Morn', 
                         'Randal', 'Stedd'],
                "female": ['Arveene', 'Esvele', 'Jhessail', 'Kerri', 'Lureene', 'Miri', 'Rowan',
                           'Shandri', 'Tessele']
            },
            "last_name": ['Amblecrown', 'Buckman', 'Dundragon', 'Evenwood', 'Greycastle', 'Tallstag']
        }, 
        'Damaran': {
            "first_name": {
                "male": ['Bor', 'Fodel', 'Glar', 'Grigor', 'Igan', 'Ivor', 'Kosef', 'Mival', 'Orel', 
                         'Pavel', 'Sergor'],
                "female": ['Alethra', 'Kara', 'Katernin', 'Mara', 'Natali', 'Olma', 'Tana', 'Zora']
            },
            "last_name": ['Bersk', 'Chernin', 'Dotsk', 'Kulenov', 'Marsk', 'Nemetsk', 
                          'Shemov', 'Starag']
        }, 
        'Illuskan': {
            "first_name": {
                "male": ['Ander', 'Blath', 'Bran', 'Frath', 'Geth', 'Lander', 'Luth', 'Malcer', 
                         'Stor', 'Taman', 'Urth'],
                "female": ['Amafrey', 'Betha', 'Cefrey', 'Kethra', 'Mara', 'Olga', 'Silifrey', 
                           'Westra']

            },
            "last_name": ['Brightwood', 'Helder', 'Hornraven', 'Lackman', 'Stormwind', 'Windrivver']
        }, 
        'Mulan': {
            "first_name": {
                "male": ['Aoth', 'Bareris', 'Ehput-Ki', 'Kethoth', 'Mumed', 'Ramas', 'So-Kehur', 
                         'Thazar-De', 'Urhur'],
                "female": ['Arizima', 'Chathi', 'Nephis', 'Nulara', 'Murithi', 'Sefris', 'Thola', 
                           'Umara', 'Zolis']
            },
            "last_name": ['Ankhalab', 'Anskuld', 'Fezim', 'Hahpet', 'Nathandem', 'Sepret', 'Uuthrakt']
        }, 
        'Rashemi': {
            "first_name": {
                "male": ['Borivik', 'Faurgar', 'Jandar', 'Kanithar', 'Madislak', 'Ralmevik', 
                         'Shaumar', 'Vladislak'],
                "female": ['Fyevarra', 'Hulmarra', 'Immith', 'Imzel', 'Navarra', 'Shevarra', 
                           'Tammith', 'Yuldra']
            },
            "last_name": ['Chergoba', 'Dyernina', 'Iltazyara', 'Murnyethara', 'Stayanoga', 'Ulmokina']
        }, 
        'Shou': {
            "first_name": {
                "male": ['An', 'Chen', 'Chi', 'Fai', 'Jiang', 'Jun', 'Lian', 'Long', 'Meng', 'On', 
                         'Shan', 'Shui', 'Wen'],
                "female": ['Bai', 'Chao', 'Jia', 'Lei', 'Mei', 'Qiao', 'Shui', 'Tai']
            },
            "last_name": ['Chien', 'Huang', 'Kao', 'Kung', 'Lao', 'Ling', 'Mei', 'Pin', 'Shin', 
                          'Sum', 'Tan', 'Wan']
        },
        'Turami': {
            "first_name": {
                "male": ['Anton', 'Diero', 'Marcon', 'Pieron', 'Rimardo', 'Romero', 'Salazar', 
                         'Umbero'],
                "female": ['Balama', 'Dona', 'Faila', 'Jalana', 'Luisa', 'Marta', 'Quara', 'Selise', 
                           'Vonda']
            },
            "last_name": ['Agosto', 'Astorio', 'Calabra', 'Domine', 'Falone', 'Marivaldi', 'Pisacar', 
                          'Ramondo']
        }
    }
    ethnicities = ['Calishite', 'Chondathan', 'Damaran', 'Illuskan', 'Mulan', 'Rashemi', 'Shou', 
                   'Tethyrian', 'Turami']
    
    def _get_ethnicity(self) -> dict:
        return self.data.get("Chondathan" if (eth := self.ethnicity) == "Tethyrian" else eth)

    def __init__(self, gender: Literal["female", "male"]) -> None:
        self.gender = gender
        self.ethnicity = choice(self.ethnicities)
        self.first_name = self.generate_first_name()
        self.last_name = self.generate_last_name()
    
    def generate_first_name(self) -> str:
        return choice(self._get_ethnicity().get("first_name").get(self.gender))

    def generate_last_name(self) -> str:
        return choice(self._get_ethnicity().get("last_name"))
    
    def __str__(self) -> str:
        return f"{self.last_name} {self.first_name}" if self.ethnicity == "Shou" else f"{self.first_name} {self.last_name}"
    
    def to_json(self) -> dict:
        return {
            "gender": self.gender,
            "ethnicity": self.ethnicity,
            "first_name": self.first_name,
            "last_name": self.last_name
        }

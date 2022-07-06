import helper as h
from time import sleep
from os import system
import random

def incorrect_input(out: str = "Неправильный номер, попробуйте ещё раз"):
    print(out)
    sleep(2)
    system('cls')

print("Выберете гениратор:\n1) Генератор NPC")
while True:
    try:
        n = int(input())
        if n == 1:
            char_class = random.choice(h.classes)
            char_race = random.choice(h.races)
            char_is_woman = random.choice((True, False))
            if char_is_woman:
                char_name = random.choice(h.female_names)
            else:
                char_name = random.choice(h.male_names)
            char_surname = random.choice(h.surnames)
        else:
            incorrect_input()
    except ValueError:
        incorrect_input()

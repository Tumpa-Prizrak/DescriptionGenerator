import filer
from helper import *


def incorrect_input():
    print(colorama.Fore.RED + "Неправильный номер, попробуйте ещё раз")


def info():
    print("Выберете генератор:\n1) Генератор персонажей\n2) Генератор названий\n3) Генератор городов")
    print(colorama.Fore.RED + "Введите quit, чтобы выйти\n" +
          colorama.Fore.YELLOW + "Введите list, чтобы показать это сообщение ещё раз\n" +
          colorama.Fore.GREEN + "Введите info, чтобы увидеть полную информацию о предыдуем объекте")


if __name__ == "__main__":
    colorama.init(autoreset=True)
    info()
    last_function_called = None
    while True:
        try:
            n = input(">")
            if n == "1":
                np = NPC()
                n.print_full_info()
                last_function_called = np
            elif n == "2":
                na = Name()
                last_function_called = na
            elif n == "3":
                town = Town()
                town.print_full_info()
                last_function_called = town
                print(colorama.Fore.YELLOW + "Введите join, если ваши игроки решат войти в таверну или церковь")
            elif n in ('q', 'quit', 'e', 'exit'):
                break
            elif n in ('list', 'l', 'spis', 's'):
                info()
            elif n in ('info', 'i'):
                filer.output_full_info(last_function_called, beutiful=True)
            elif n in ('join', 'j'):
                filer
            else:
                incorrect_input()
        except ValueError:
            incorrect_input()

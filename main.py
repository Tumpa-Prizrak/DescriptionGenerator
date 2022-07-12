from helper import *


def incorrect_input():
    print(colorama.Fore.RED + "Неправильный номер, попробуйте ещё раз")


def info():
    print("Выберете генератор:\n1) Генератор персонажей\n2) Генератор названий\n3) Генератор городов")
    print(colorama.Fore.RED + "Введите quit чтобы выйти\n" +
          colorama.Fore.YELLOW + "Введите list чтобы показать это сообщение ещё раз")


if __name__ == "__main__":
    colorama.init(autoreset=True)
    info()
    last_function_called = None
    while True:
        try:
            n = input(">")
            if n == "1":
                NPC().print_full_info()
            elif n == "2":
                print(Name())
            elif n == "3":
                town = Town()
            elif n in ('q', 'quit', 'e', 'exit'):
                break
            elif n in ('list', 'l', 'spis', 's'):
                info()
            elif n in ('info', 'i'):
                pass
            else:
                incorrect_input()
        except ValueError:
            incorrect_input()

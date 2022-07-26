from typing import Callable

import colorama

import helper as h
import rulang as ru


def output_full_info(obj, *, tabs=0, beutiful=False):
    for i in dir(obj):
        if i.startswith("_"):
            continue
        if issubclass(type(getattr(obj, i)), Callable):
            continue
        if type(getattr(obj, i)).__name__ in dir(h):
            try:
                print("    " * tabs + ru.ru_fields[i] + ": " +  colorama.Fore.YELLOW + " {")
            except KeyError:
                print("    " * tabs + i + ": " + colorama.Fore.YELLOW + " {")
            output_full_info(getattr(obj, i), tabs=tabs + 1, beutiful=beutiful)
            print("    " * tabs + colorama.Fore.YELLOW + "}")
        elif type(getattr(obj, i)) == list and len(getattr(obj, i)) != 0:
            try:
                print("    " * tabs + ru.ru_fields[i] + ": " + colorama.Fore.YELLOW + " [")
            except KeyError:
                print("    " * tabs + i + ": " + colorama.Fore.YELLOW + " [")
            for o in getattr(obj, i):
                output_full_info(o, tabs=tabs + 1, beutiful=beutiful)
                print()
            print("    " * tabs + colorama.Fore.YELLOW + "]")
        else:
            if str(getattr(obj, i)) in ("[]", "{}"):
                try:
                    print("    " * tabs + ru.ru_fields[i] + ": " + colorama.Fore.YELLOW + str(getattr(obj, i)))
                except KeyError:
                    print("    " * tabs + i + ": " + colorama.Fore.YELLOW + str(getattr(obj, i)))
            else:
                try:
                    print("    " * tabs + ru.ru_fields[i] + ": " + colorama.Fore.GREEN + str(getattr(obj, i)))
                except KeyError:
                    print("    " * tabs + i + ": " + colorama.Fore.GREEN + str(getattr(obj, i)))

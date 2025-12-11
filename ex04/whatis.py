import sys


def whatis():
    args = sys.argv

    if len(args) != 2:
        if len(args) > 2:
            print("AssertionError: more than one argument is provided")
        return

    if not args[1].isdigit():
        print("AssertionError: argument is not an integer")
        return

    num = int(args[1])
    if (num % 2) == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


whatis()

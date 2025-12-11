import sys


def get_input() -> str:
    """
        check argeument amount.
        if it's 0, start to get get unput on stdin.

        Returns:
            str: imput stracture value
    """
    args = sys.argv

    if len(args) > 2:
        raise AssertionError("more than one argument is provided")
    elif len(args) == 2:
        return args[1]

    else:
        print("What is the text to count?")

        try:
            st_input = sys.stdin.read()
        except Exception:
            raise AssertionError("Input reading failed")

        str = st_input.replace('\n', ' ')

        if not str:
            raise AssertionError("argument is missing from stdin")
        return str


def count_type(text: str):
    """
        get stracture and
        count the type of char in it.
    """

    counts = {
        "digit": 0,
        "upper": 0,
        "lower": 0,
        "space": 0,
        "punct": 0
    }

    for char in text:
        if char.isdigit():
            counts["digit"] += 1
        elif char.isupper():
            counts["upper"] += 1
        elif char.islower():
            counts["lower"] += 1
        elif char == ' ':
            counts["space"] += 1
        else:
            counts["punct"] += 1

    print(f"The text contains {len(text)} characters:")
    print(f"{counts['upper']} upper letters")
    print(f"{counts['lower']} lower letters")
    print(f"{counts['punct']} punctuation marks")
    print(f"{counts['space']} spaces")
    print(f"{counts['digit']} digits")


def main():
    try:
        input_str = get_input()
        count_type(input_str)

    except AssertionError as e:
        print(f"AssertionError: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()

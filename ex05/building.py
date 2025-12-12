import sys


def get_input() -> str:
    """
    Gets input string either from command-line argument or stdin.

    Raises:
        AssertionError: If more than one argument is provided.
        AssertionError: If reading from stdin fails.
        AssertionError: If the argument is missing from stdin.

    Returns:
        str: The processed input string.
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
    Counts and prints the number of different character types in the input.

    Character types counted are: uppercase, lowercase, punctuation,
                                 space, and digit.

    Args:
        text (str): The string whose characters are to be counted.
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
    """
    Main function to handle input,
    count character types, and manage exceptions.
    """
    try:
        input_str = get_input()
        count_type(input_str)

    except AssertionError as e:
        print(f"AssertionError: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()

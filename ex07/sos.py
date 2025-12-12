import sys


def encode_to_morse(text: str) -> str:
    """
    Encodes the given string into Morse Code.

    Args:
        text (str): The original string to be encoded.

    Returns:
        str: The string converted to Morse Code.
    """
    if not isinstance(text, str):
        raise AssertionError("The argument must be a string (str).")

    MORSE_CODE_DICT = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
        'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        ' ': '/'
    }

    text = text.upper()
    morse_output = []

    for char in text:
        if char in MORSE_CODE_DICT:
            morse_char = MORSE_CODE_DICT[char]
            morse_output.append(morse_char)
        elif char.isalnum() or char.isspace():
            pass
        else:
            print(f"Character '{char}' is not supported")

    return " ".join(morse_output)


def main():
    """
    The main entry point of the program.
    It handles command-line arguments, calls the encoding function,
    and prints the result, including error handling.
    """
    args = sys.argv

    try:
        if len(args) != 2:
            raise AssertionError("Invalid number of arguments.")

        input_string = args[1]

        morse_result = encode_to_morse(input_string)

        print(morse_result)

    except AssertionError as e:
        print(f"AssertionError: {e}", file=sys.stderr)
        sys.exit(1)

    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

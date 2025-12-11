import sys


is_digit_lam = lambda s: s.isdigit()


def check_arg(args:list) -> tuple:
    """
        check command line
        if it's valied, return contents

        Return: tuple (text, num)
    """
    if len(args) != 3:
        raise AssertionError("the arguments are bad")

    text_s = args[1]
    num_s = args[2]

    if not text_s.isalpha() or not is_digit_lam(num_s):
        raise AssertionError("the arguments are bad")
    return text_s, num_s


def filter_string(text_s: str, num_s: str) -> list:
    """
    filter string by number and return result

    Return: list
    """
    n = int(num_s)
    str_list = text_s.split(" ")
    res_list = [word for word in str_list if len(word) > n]
    return res_list


def main():
    args = sys.argv
    try:
        text_s, num_s = check_arg(args)
        res_list = filter_string(text_s, num_s)
        print(res_list)

    except AssertionError as e:
        print(f"AssertionError: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()

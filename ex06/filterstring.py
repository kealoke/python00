import sys


def check_arg(args: list) -> tuple:
    """
    Checks command-line arguments for validity.

    Validates that exactly two arguments are provided and that they are of the
    correct type (string S and integer N).

    Args:
        args (list): The list of command-line arguments.

    Raises:
        AssertionError: If the number of arguments is not 2.
        AssertionError: If the argument types are incorrect.

    Returns:
        tuple: A tuple containing the valid string and the number  as strings.
    """
    if len(args) != 3:
        raise AssertionError("the arguments are bad")

    text_s = args[1]
    num_s = args[2]

    if not text_s.isalpha() or not num_s.isdigit():
        raise AssertionError("the arguments are bad")
    return text_s, num_s


def filter_string(text_s: str, num_s: str) -> list:
    """
    Filters a string and returns words longer than a specified number.

    Splits the input string into words and uses list comprehension to return
    a list of words whose length is strictly greater than the integer N.

    Args:
        text_s (str): The input string (S).
        num_s (str): The number (N) as a string, defining the minimum length.

    Returns:
        list: A list of words from S whose length is > N.
    """
    n = int(num_s)
    str_list = text_s.split(" ")
    res_list = [word for word in str_list if len(word) > n]
    return res_list


def main():
    """
    Main function to process command-line arguments
    and run the filtering logic.

    Handles argument validation and filtering, outputting the result or
    printing an AssertionError message if validation fails.
    """
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

import os
from time import sleep
from tqdm import tqdm


def format_time(seconds):
    """
    Formats time in seconds into MM:SS or HH:MM:SS string format.

    Args:
        seconds (float or int): The time duration in seconds.

    Returns:
        str: The formatted time string (e.g., '02:30' or '01:05:10').
    """
    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)
    if h > 0:
        return f"{h:02d}:{m:02d}:{s:02d}"
    return f"{m:02d}:{s:02d}"


def ft_tqdm(lst: range):
    """
    Custom implementation of a progress bar similar to tqdm.

    This function iterates over an iterable, updates a progress bar
    on the console line using carriage returns, and yields each item.

    Args:
        lst (range): The iterable (typically range) to wrap and iterate over.

    Yields:
        The elements of the input iterable 'lst'.
    """
    total = len(lst)

    try:
        terminal_width = os.get_terminal_size().columns
    except OSError:
        terminal_width = 80

    NON_BAR_LENGTH = 45
    BAR_WIDTH = terminal_width - NON_BAR_LENGTH
    BAR_WIDTH = max(10, BAR_WIDTH)

    for i, item in enumerate(lst):
        current_iter = i + 1
        percent = (current_iter / total) * 100
        filled_len = int(BAR_WIDTH * current_iter // total)

        # create progress bar
        bar = '=' * filled_len
        if filled_len < BAR_WIDTH:
            bar += '>'
            bar += ' ' * (BAR_WIDTH - len(bar))

        # create output string
        output = (
            f"{percent:3.0f}%|"
            f"[{bar}]| "
            f"{current_iter}/{total} "
        )

        # back to the head by \r  and overwrite
        print('\r' + output, end='', flush=True)

        yield item

    # lastline
    final_bar = '=' * BAR_WIDTH
    final_output = (
        f"100%|"
        f"[{final_bar}>]| "
        f"{total}/{total} "
    )
    print('\r' + final_output, flush=True)


def main():
    """
    Demonstrates and compares the custom ft_tqdm with the standard tqdm.
    """
    for elem in ft_tqdm(range(333)):
        sleep(0.005)
    print()

    for elem in tqdm(range(333)):
        sleep(0.005)
    print()


if __name__ == "__main__":
    main()

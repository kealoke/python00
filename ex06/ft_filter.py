def ft_filter(function, iterable):
    """
    Filter elements from an iterable using a function.

    Returns an iterator yielding those items of iterable for which the
    corresponding item is true. If function is None, returns the items
    that are inherently true (not zero, empty, or None).

    Args:
        function: A function to test each element of the iterable.
                  Can be None.
        iterable: The iterable sequence to filter.

    Yields:
        The items from the iterable that satisfy the condition.
    """
    if not function:
        return (item for item in iterable if item)
    return (item for item in iterable if function(item))

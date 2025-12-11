def ft_filter(function, iterable):
    if not function:
        return (item for item in iterable if item)
    return (item for item in iterable if function(item))

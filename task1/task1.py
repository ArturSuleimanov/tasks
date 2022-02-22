def round_array_rout(n, m):
    """
    >>> round_array_rout(5, 4)
    14253
    >>> round_array_rout(4, 3)
    13
    """
    route = [None]
    i = 1
    while True:
        i = 1 + (i + m - 2) % n
        if i == 1:
            break
        route.append(i)
    route[0] = 1
    print(''.join(map(str, route)))



DEBUG = False


if not DEBUG:
    n, m = map(int, input().split())
    round_array_rout(n, m)
else:
    import doctest
    doctest.testmod()

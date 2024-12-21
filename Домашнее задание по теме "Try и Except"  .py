def add_everything_up(a, b):
    try:
        return a + b
    except TypeError:
        return f'{a}{b}'

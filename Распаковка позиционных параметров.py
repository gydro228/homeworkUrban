def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()
print_params(25)
print_params(c=[1, 2, 3])
print_params(42, 'текст', False)

values_list = [3, 'арбуз', False]
values_dict = {'a': 10, 'b': 'hello', 'c': True}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)

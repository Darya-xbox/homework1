def print_params(a=1, b='строка', c=True):
    print(a, b, c)
    values_list_2 = (2, 'слива')

print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [2, 'столбец', False]
values_dict = {'a': 3, 'b': 'слово', 'c': False}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ('Хай', 52)
print_params(*values_list_2, 42)
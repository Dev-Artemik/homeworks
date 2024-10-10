def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(9, "СтРоКа", False)
print_params(95, 'STROKA', True)

print_params(b = 25)
print_params(c = [1,2,3])

values_list = [984, 'sdas', 526.25]
values_dict = {
    'a': 8956,
    'c': False,
    'b': 'strochka'
}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [3, 3.68]
print_params(*values_list_2, 42)


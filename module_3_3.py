def print_params(a = 1, b = 'строка', c = True):
  print(a, b, c)

print_params()
print_params(3)
print_params(5, 'test')
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [True, 'example', 78.25]
values_dict = {'a':44, 'b': False, 'c': 542.05}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)
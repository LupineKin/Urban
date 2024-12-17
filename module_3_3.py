def print_params(a = 1, b = 'строка', c = True):
    print (a, b, c)
print_params()
values_list = [2, 'bbb', False]
print_params(*values_list)
values_dict = {'a':1.1 , 'b': 'строка', 'c': False}
print_params(**values_dict)
values_list_2 = ['ff', 1234]
print_params(*values_list_2, 45)
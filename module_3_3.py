def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


values_list = ['ABC',False,5.25]
values_dict = {'a': 'stroka99', 'b': 123, 'c': False}
values_list_2 = [54.32, 'Строка']

print_params() # первое обращение без аргументов
print_params(25) # второе обращение с 1 аргументом
print_params('str',99) # второе обращение с 3 аргументами
print_params(3,2,1) #меняем все 3 аргумента
print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
#  Работа со словарями
print('Работа со словарями:'.upper())
my_dict = {'Alex':1900, "Ben": 1910, 'Chris': 1905, 'Richard': 2000, "Bill": 1955}
print('Dict:',my_dict)

print('The Year is:',my_dict['Chris'])
print('AV - ',my_dict.get('AV','Нет такого ключа'))
my_dict.update({'Serg': 1968,
                   'Michael': 1940})
# print('Modified dictionary:',my_dict)
a = my_dict.pop('Ben')
print('Been Deleted a Year:',a)
print("The last updated Dict:",my_dict)

# Работа с множествами
print('Работа с множествами:'.upper())
my_set = {8, 1, 2, 3, 4, 5, 1, 2, 3, 6, 'String', True, (1, 2, 3)}
print('Set:',my_set)
my_set.update([7,55])
print('Updated Set:',my_set)
a = my_set.discard('String')
print('Set after Delete',my_set)
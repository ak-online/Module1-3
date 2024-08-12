#food = ['яблоко','кокос','банан','манго']
#print(food)
#food.append('молоко')
#print(food)
#food.extend(['мясо', True])
#print(food)
#food.remove('мясо')
#print(food)
#print('кокос' not in food)
#print(food[0:4:2])

# p.1
immutable_var = 2001, 2002, 2003, 'Year', 'Century', True
print(immutable_var )

#p.2
# immutable_var[2] = 2003 - кортеж не поддерживает обращение по элементам.
print(immutable_var[2]) # unchanged

#p3
mutable_list = [1,2,3,'манго', 2024, True]
print(mutable_list)
mutable_list[3] = 2000
print(mutable_list)
mutable_list.extend(['сок', False])
print(mutable_list)
mutable_list.append('молоко')
print(mutable_list)
print('кокос' in mutable_list)
print('кокос' not in mutable_list)
print(mutable_list[0:5:2])
mutable_list = ([1,2,3],'манго', 2024, True)
print(mutable_list)
mutable_list[0][0]=10
print(mutable_list)
mutable_list_plus = mutable_list + (55,66)
print(mutable_list_plus)
mutable_list_new = mutable_list_plus * (3)
print(mutable_list_new)
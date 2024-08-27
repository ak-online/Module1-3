# data_structure = [
#   [1, 2, 3],
#   {'a': 4, 'b': 5},
#   (6, {'cube': 7, 'drum': 8}),
#   "Hello",
#   [1, 2, 3],
#   {'a': 4, 'b': 5},
#   ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_sum(data):
    res = 0
    for item in data:
        # print('Item', item, type(item), isinstance(item, list), isinstance(item, tuple), isinstance(item, set))
        if isinstance(item, list) :
            res += calculate_sum(item)
        if isinstance(item, tuple) :
            res += calculate_sum(item)
        if isinstance(item, set):
            res += calculate_sum(item)
        if isinstance(item, dict):
            res += calculate_sum(item.items())
        if isinstance(item, int or float):
            res += item
        elif isinstance(item, str):
            res += len(item)
    return res

answer = calculate_sum(data_structure)
print(answer)
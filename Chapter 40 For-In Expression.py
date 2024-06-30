# all_nums = [-3, 1, 0, 10, -20, 5]

# absolute_nums = [abs(item) for item in all_nums]

# print(absolute_nums)


# nums = [10, 2, 5, 100]

# squard_nums = []

# for num in nums:
#     squard_nums.append(pow(num,2))


# print(squard_nums)

# squard_nums = [pow(num,2) for num in nums]

# print(squard_nums)


# fruits = ['banana', 'mandarin', 'orange', 'apple']


# fruit_lenght = {item: len(item) for item in fruits}

# print(fruit_lenght)


# names = ['asdf', 'alex', 'asdfasdf']

# names_lengths = tuple(len(item) for item in names)

# print(names_lengths)


# cordinates = (120, 240, 500)

# coor_list = [item * 2 for item in cordinates]

# print(coor_list)



# grades = (80, 95, 65)
# sub = ['Science', 'Math', 'Physics']

# # print(dict(zip(sub, grades)))

# grate_dict = { s: g -10 for s,g in zip(sub, grades)}

# print(grate_dict)


# foo = [(1,2), (2,3)]


# for k,v in foo:
#     print(k, v)


# person = {
#     'name': "asfa",
#     "num": 67,
#     "instructor": True
# }


# person_str =  [item for item in person.values() if type(item)==str]

# print(person_str)

# stocks = {
#     'Google': 1500, 
#     'AMZN': 3000,
#     'APPLE': 300
# }

# douled_stocke = { k: v * 2 for k,v in stocks.items() if v >= 500 }

# print(douled_stocke)



# foo = {
#     "name": "Alex",
#     "position": "homless",
#     "car": "nop"
# }


# foo1 = { k.upper(): v for k,v in foo.items() }

# print(foo1)


# foo1 = ['asdfasdf','adf', 'lolsssss', 'aaadasddick']
# foo2 = [item for item in foo1 if len(item) > 5]

# foo2.reverse()


# print(foo2)



nested_list = [[1,2,3], [4,5,6], [7,8,9]]
flaten = [item for item in nested_list for item in item ]


print(flaten)



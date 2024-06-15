""" all_nums = [-3,1,0,10,-20,5]

absolute_nums = [abs(item) for item in all_nums]

print(absolute_nums)

print(all_nums) """


""" all_nums = [-3, 1, 0 , 10 , -20, 5]

positive_nums = []

for num in all_nums:
    if num > 0:
        positive_nums.append(num)


print(positive_nums)

print(all_nums) """


""" all_nums = [-3, 1,0,10,-20,5]

positive_nums=[ num for num in all_nums if num > 0 ]

print(positive_nums)
print(all_nums)  """


""" my_set = {1,10, 15}

new_set = set()


for val in my_set:
    new_set.add(val*val)

print(my_set)

print(new_set) """


""" my_set = {1,10,15}

new_set = {item* item for item in my_set}

print(new_set)
print(my_set) """



""" my_scores = {
    'a': 10,
    'b':7,
    'm':14
}


scores = {}

for k, v in my_scores.items():
    scores[k] = v


print(scores)

print(my_scores) """




""" my_scores = {
    'a': 10,
    'b': 7,
    'm': 14
}

scores = {k: v * 10 for k,v in my_scores.items()}


print(my_scores)

print(scores) """

""" nums = [10, 2, 5, 100]


squared_nums = [pow(num,2) for num in nums]

"" for item in nums:
    squared_nums.append(pow(item,2)) """

#print(squared_nums) 




""" fruits = ['banana', 'mandarin', 'orange', 'apple']


fruit_lenght = {item: len(item) for item in fruits}

print(fruit_lenght) """


""" names = ['Bogdan', 'Alice', 'Bob']

new_names = tuple(len(item) for item in names)


print(new_names) """


""" coordinates = (120, 240, 500)

coordinates_list = [pow(item, 2) for item in coordinates]


print(coordinates_list) """











 

  




 

 




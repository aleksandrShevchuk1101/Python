
# my_fruits = ["apple", "banana", "lime"]
# posts_ids = [151, 245, 762, 167]
# user_inputs = [True, "hi!", 10.5]


# print(my_fruits)

# del my_fruits[0]
# print(my_fruits)
# print(len(my_fruits))


# users = [
#     {
#         "user_id": 134,
#         "user_name": "Alice"
#     },
#     {
#         "user_id": 831,
#         "user_name": "Bob"
#     }
# ]

# print(len(users))
# print(users[1]["user_name"])


# inp = [True, "Hi!", 'asdf', 10.5]

# inp.pop()
# print(inp)

# inp.pop(0)
# print(inp)


# posts_ids = [245, 151, 762, 167]

# posts_ids.sort()

# print(posts_ids)

# posts_ids.sort(reverse=True)

# print(posts_ids)

# greeting = "Hello from Python"

# foo = list(greeting)

# print(foo)


# ratings = [2.5, 5.0, 4.3, 3.7]

# print(min(ratings))
# print(max(ratings))
# print(sum(ratings))

# print(sum(ratings) / len(ratings))


#my_nums = [10, 3, 100, 35]

# print(my_nums)
# print(type(my_nums))
# print(isinstance(my_nums, list))
# print(id(my_nums))


#print(my_nums[0], my_nums[-1], my_nums[2])


#my_nums.append(50)

# my_nums.pop()
# print(my_nums)

# my_nums = [10, 3 , 100, 35]
# merge_nums = [1, 4, 3, 2]

# #my_nums.extend('absadf')

# foo = my_nums + merge_nums

# # my_nums.clear()



# print(foo)

# my_cars = ["BMW", "Mersedes"]


# copied_cars = list(my_cars)  # built in fuction
# #copied_cars = my_cars[:]  # slice
# #copied_cars = my_cars.copy()  

# copied_cars.append("Audi")

# print(copied_cars)

# print(my_cars)

# print(id(my_cars) == id(copied_cars))




# my_list = [1, 2.0, "asf", [1,2,3,4] , {"one": 1}]

# my_list.pop(3)

# print(len(my_list))

# my_list.reverse()
# print(my_list)

# my_list_2 = [1,2,3,4,5,6,76]
# my_list.extend(my_list_2)
# print(my_list)

first_list = [1, 2, 3, 4, 5, 6]
second_list = [7, 8, 9, 10, 11, 12]
#combine_list = first_list.__add__(second_list)

combine_list = first_list[:]
combine_list = combine_list.__add__(second_list)

print(combine_list)

# def mult_by(multiplier):
#     return lambda x: x * multiplier


# multiply_by_3 = mult_by(3)

# print(multiply_by_3)
# print(type(multiply_by_3))


# print(multiply_by_3(3))
# print(multiply_by_3(5))



# students = [
#     {'name': 'John','score' : 80},
#     {'name': 'Alice', 'score' : 20},
#     {'name': 'Alex', 'score' : 50}
# ]

# # def foo(l):
# #     return l['score']

# # students.sort(key=foo)



# students.sort(key= lambda l: l['name'], reverse=True)

# print(students)


my_nums = [3, 4, 10, 15, 20, 21]

even_nums = list(filter(lambda num: num % 2 == 0, my_nums))

odd_nums = list(filter(lambda x: x % 2 == 1, my_nums))

print(even_nums)
print(odd_nums)

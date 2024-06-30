

# nums = (3,5,10)

# squares = (nums * nums for item in nums)

# print(type(squares))



# from sys import getsizeof

# squares_gen = (num * num for num in range(1000_000_00))

# print(getsizeof(squares_gen))

# print(type(squares_gen))

# squares_list = [num * num for num in range(1000_000_00 )]

# print(getsizeof(squares_list))
# print(type(squares_list))


squares_gen = (num * num for num in range(1000_000))

for num in squares_gen:
    print(num)
    if num == 1000:
        break
        





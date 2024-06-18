
# my_fruits = {'apple', 'banana', 'lime'}

# posts_ids = {151, 245, 762, 167}

# user_inputs = {True, 'hi!', 'af', 10.5}


# print(my_fruits)
# print(type(posts_ids))


# posts_ids = {151, 245, 167, 167, 151}

# print(posts_ids)

# print(type(posts_ids))


# my_fruits = {'apple', 'banana', 'lime'}

# other_fruits = {'lime','apple', 'banana'}

# print(my_fruits == other_fruits )

# print(my_fruits)

# my_fruits = {'apple', 'banana', 'lime'}
# print(len(my_fruits))

# posts_ids = {151, 245, 167, 167, 151}
# print(len(posts_ids))

# lists_set = {[1,2], [20,5]}


# my_set = {10, 5, 5, 100, 10, 20}

# print(my_set)
# print(type(my_set))
# print(isinstance(my_set, set))
# print(len(my_set))


# photo_sizes = {'1920x1080', '800x600'}
# photo_sizes.add('sdfsadf')

# print(photo_sizes)

# photo_sizes = {'1920x1080', '800x600'}
# other_sizes = {'800x600', '1024x768'}

# # all_sizes = photo_sizes.union(other_sizes)

# # print(all_sizes)  # '1920x1080', '800x600', '1024x768'

# common_sizec = photo_sizes.intersection(other_sizes)
# print(common_sizec)


# nums = {10, 5 , 35}

# other_nums = {20,5,12,10,35}
# # res = nums.issubset(other_nums)
# # print(res)


# res = other_nums.issuperset(nums)
# print(res)


# () - Tuples
# {} - set
# [] - list
# {} - dictinory


# my_set = {10, 2, 10, 5, 7}

# print(my_set)

# my_set.add(8)

# print(my_set)

# my_set.discard(200)
# print(my_set)


# my_set = {10, 2, 10, 5, 7}
# other_set = {34, 1, 10, 5}

# print(my_set.intersection(other_set))
# print(other_set.intersection(my_set))

# print(my_set & other_set)



# my_set = {10, 2, 10, 5, 7}
# other_set = {34, 1, 10, 5}

# print(my_set.union(other_set))
# print(other_set.union(my_set))
# print(my_set | other_set)

# set_copy = other_set.copy()
# set_copy.add(200)
# print(other_set)
# print(set_copy)



# my_set = {'a', 'c', 'd'}
# other_set = {'l', 'm', 'c'}
# print(my_set.symmetric_difference(other_set))


my_set = {1,2,3}

#my_set.add(4)

other_set = {2,3,4,5,6,7}

new_set = my_set.intersection(other_set)

print(new_set)
print(type(my_set))

my_list = list(new_set)
print(my_list)

print(my_set.difference(other_set))
print(other_set.difference(my_set))




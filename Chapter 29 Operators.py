# my_num = False

# print(my_num)
# print(+ my_num)
# print(- my_num)


# my_name = "dlsfals"

# print(my_name)
# print(not not my_name)
# print(bool(my_name))


# my_list = []

# print(not my_list)


first_set = {2,4}
second_set = {4,2}


# second_set = first_set

if (first_set == second_set):
    print("The variables are equel")
else:
    print("The variables are not equel")

print(id(first_set))
print(id(second_set))
print(first_set is second_set)
print("-------------------------------")

if 10 in first_set:
    print("We have")
elif 10 not in first_set:
    print("We don't have")

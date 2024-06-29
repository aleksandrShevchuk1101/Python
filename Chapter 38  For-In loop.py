# coutries = ["USA", "Canada", "UK", "Australia"]

# for a in coutries:
#     print(f"Welcome to {a}")



# months = ("Jan", "Feb", "Apr", "September")

# for item in months:
#     print(item)


# foo = {
#     'PC': 1000,
#     'Mobile Phone': 200,
#     'Tablet': 350,
#     'Camera': 700
# }

# for k in foo:
#     print(k)
#     print(foo[k])

# for item in foo.items():
#     print(item)

# for k,v in foo.items():
#     print(k,v)

# name = 'Jennifer'

# for char in name:
#     print(char)


# for i in range(10,-1,-1):
#     print(i)

# print("Racket launch")

# foo = {'romance', 'fantasy', 'comedy', 'Science Fiction'}


# for item in foo:
#     print(item)



# def dict_2_list(foo: dict):

#     if not type(foo) is dict:
#         raise TypeError("Wrong type")
    
#     foo1 = []

#     for k,v in foo.items():
#         temp = (k,  v *2 if type(v) is int else v)
#         foo1.append(temp)
        


#     return foo1


# foo = {
#     "one" : 1,
#     "two" : "sdfasdf",
#     "three" : 3,
#     "four" : 'sdafasdf'
# }

# foo1 = {
#     "one" : 234,
#     "two" : 234,
#     "three" : False,
#     "four" : 33.2
# }


# try:
#     print(dict_2_list(foo))
#     print(dict_2_list(foo1))
# except Exception as e:
#     print(e)
# else:
#     print("Success")
# finally:
#     print("Finaly block")


# def filter_list(foo1: list, foo2):

#     type1 = type(foo1)
#     type2 = type(foo2)

#     if type1 is not list:
#         print("Error")
#         return []

#     foo = []

#     for item in foo1:
       
#        if type(item) == type(foo2):
#             foo.append(item)


#     return foo



# data = [354,"hjfhgj", 23.5, False, 22.6, 'asdf', 12234, 53535, (2,3,4,5,6)]
# print(filter_list(data, 1243))
# print(filter_list(data, bool))
# print(filter_list(data, float))
# print(filter_list(data, str))
# print(filter_list(data, tuple))


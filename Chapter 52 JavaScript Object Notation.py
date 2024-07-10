# import json 


# my_nums = [10, 100, 5, 20]


# res = json.dumps(my_nums)

# print(res)
# print(type(res))



# my_nums = {10, 100, 5, 20}
# my_nums = (10, 100, 5, 20)


# res = json.dumps(my_nums)

# print(res)
# print(type(res))

#dict 

# my_post = {
#     'title': "My post",
#     'content': "Post content",
#     'likes_qty': 25,
#     'author': {
#         'user_name': 'bogdan123',
#         'email': 'b@gmail.com'
#     },
#     'metadata': (5,7,20)
# }

# foo = json.dumps(my_post)

# print(foo)
# print(type(foo))


# my_post_dict = json.loads(foo)
# print(my_post_dict)
# print(type(my_post_dict))



# def sum_fn(a,b):
#     return a + b




# my_math = {
#     'title': "Math dict",
#     'sum': sum_fn
# }



# import json

# my_dict = {
#     'name': 'Bogdan',
#     'is_instructor': True   
# }

# #print(my_dict)
# my_dict_json = json.dumps(my_dict, indent=2)

# file = open('test.txt', 'w')
# file.write(my_dict_json)


import json

# foo = {
#     'one': '1',
#     'two': 2,
#     'three': True,
#     'four': 1.2,
#     'five': [1,2,3,4,5,6],
#     'six': ('dsfafd', 'asdfasdf', 12, True),
#     'seven' : None,
#     'eight': {
#         'name': 'asfdas',
#         'sername': 12
#     }
# }

# foo_json = json.dumps(foo, indent=3)

# print(foo_json)
# print(type(foo_json))


foo_list = [
        {
            'one': 1,
            'two': 2,
            'three': [12,23,35],
            'four': (123,123,34),
            #'five': {12,23,34}
        },
        {
            'sadf': 'asdf',
            'ewrdf': 1,
            'three': 3
        }
]

foo_json = json.dumps(foo_list)
print(foo_json)


foo_list = json.loads(foo_json)


print(foo_list)
print(type(foo_list))











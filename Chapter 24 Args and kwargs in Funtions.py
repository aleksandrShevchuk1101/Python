

# def sort_nums(*args):
#     # print(args)
#     # print(type(args))
#     # args.append(10)
#     for item in args:
#         print(item)

# def foo(*item):
#     return sorted(item)

# sorted_nums = foo(10, 3, 15, 246) 
# print(sorted_nums)


# def get_posts_info(name, posts_qty):
#     info = f"{name} wrote {posts_qty} posts"
#     return info

# string = get_posts_info(name = "Alex", posts_qty = 25)

# print(string)


def get_posts_info(**person):
    print(person)
    print(type(person))
    
    string = ( f"{person['name']} is {person['age']}"
            f" lives in {person['city']}"
    )
    return string


print(get_posts_info(name = "Alex", age = 25, city = "Rotterdam"))

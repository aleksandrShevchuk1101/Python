

# def sort_nums(*args):
#     # print(args)
#     # print(type(args))
#     # args.append(10)
#     for item in args:
#         print(item)

def foo(*item):
    return sorted(item)

sorted_nums = foo(10, 3, 15, 246) 
print(sorted_nums)

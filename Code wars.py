


# def foo(x,y):
#     x_pos = range(0, 101)
#     x_neg = range(-100,1)
#     y_pos = x_pos
#     y_neg = x_neg

#     return 1 if x in x_pos and y in y_pos else 2 if x in x_neg and y in y_pos else 3 if x in x_neg and y in y_neg else 4



# print(foo(19,-56))


# def foo(number):
#     return "Even" if not number % 2 else "Odd"

# print(foo(0))




# def foo(a,b,c):
#     return max([a*(b+c), a*b*c, a+b*c, (a+b)*c, a+b+c])
    

# print(foo(2,1,2))
# print(foo(2,1,1))
# print(foo(2,2,4))
# print(foo(3,3,3))
# print(foo(1,1,1))



def foo(a): return "Error" if not isinstance(a,int) else a * 50 + 6

print(foo(3))
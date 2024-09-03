


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



# def foo(a): return "Error" if not isinstance(a,int) else a * 50 + 6

# print(foo(3))



# class Solution:

#     foo = 'lol'

#     def main(self, *args):
#         print("Hello world")
#         _ = foo


# foo = Solution()
# foo.foo = "dick"
# print(foo.foo)

# foo1 = Solution()
# print(foo1.foo)




# def foo(s):
#     if not isinstance(s, str):
#         raise TypeError
    
#     return s.upper()
    



# print(foo('dsf'))

# import re

# res = re.split(r'\+|=', foo)
# res = [int(item[::-1]) for item in res]

# # print(int(res[0]+int(res[1]) == int(res[2])))



# print(res[0]+res[1] == res[2])

# foo1 = [''.join(item.) for item in res]


# foo = '73+42=16'
# foo = '5+8=13'

# res = foo.replace('+',',').replace('=',',').split(',')
# res = [int(i[::-1]) for i in res]

# print(res[0] + res[1]== res[2])

# res = foo.split('[+=]')
# print(res)


#--------------------------------------------------------------
# class Dislike:
#     pass

# class Like:
#     pass

# class Nothing:
#     pass


# arr = [Dislike]
# # arr = [Like, Like]
# # arr = [Dislike, Like]


# def like_or_dislike(lst):

#     dis = False
#     like = False

#     for item in lst:
#         if type(item) is Dislike:
#             like = False
#             dis = not dis

#         if type(item) is Like:
#             dis = False
#             like = not like

#     return Dislike if dis else Like if like else Nothing

# print(like_or_dislike(arr))

#--------------------------------------------------------------

# foo = ['B', 'C', "D", F, G, H, J, K, L, M, N, P, Q, R, S, T, V, W, X, Y, Z.]

# lol = 'x' in foo

# print(lol)

# def disemvowel(string_):

#     list_of_vowels = ('a', 'e', 'i', 'o', 'u')
#     # new_string = ""

#     # for i in string_:
#     #     if i.lower() not in list_of_vowels:
#     #         new_string += i




#     return ''.join([i for i in string_ if i.lower() not in list_of_vowels])

# print(disemvowel("This website is for losers LOL!"))
# disemvowel("No offense but,\nYour writing is among the worst I've ever read")



# def lol(s):
#    for i in "aeiouAEIOU":
#         s = s.replace(i,'')

#     return s
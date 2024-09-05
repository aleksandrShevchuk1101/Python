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


# def longest(a1,a2):

#     # com_str = a1 + a2
#     # new_list = []

#     # for letter in com_str:
#     #     if letter not in new_list:
#     #         new_list.append(letter)
            
    

#     # return new_list

#     return "".join(sorted(set(a1+a2)))



# foo = "aretheyhere"
# foo1 = "yestheyarehere"


# print(longest(foo, foo1))  

# print(foo)
# print(set(foo))

# def whatday(num):
    
#     DAYS = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    
#     return DAYS[num-1] if 0 < num <= len(DAYS) else "Wrong, please enter a number between 1 and 7"


# print(whatday(0))

# def whatday(num):

#     foo = {1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 5: "Thursday", 6: "Friday", 7: "Saturday"}
    
#     return foo.get(num, "Wrong, please enter a number between 1 and 7")



# print(whatday(0))



# def last(*ar):

#     print(ar)
    
#     return None
    

# foo1 = (5,6,2,32,3232)
# foo2 = [1,2,3,4,5,6,7,8,9,10]
# foo3 = ("abckxyz")
# foo4 = ("a", "b", "c", "z")
# foo5 = (123, [4, 5, 6])
# foo6 = [1,2,3,4,5,6,7,8,9,10]






# def last(*arr):
    
#     if len(arr)==1:
#         arr= list(arr[0])
#         return arr[-1]
#     else:
#         return arr[-1]   
    

# last([1,2,3,4,5,6,7,8,9,10])
# last(5,6,2,32,3232)
# last(list("abckxyz"))
# last("abckxyz")
# last("a", "b", "c", "z")
# last(123, [4, 5, 6])
# last(1,2,3,4,5,6,7,8,9,10)
        








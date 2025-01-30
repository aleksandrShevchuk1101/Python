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


# (5, 8, 6, 4) =>  9
# (1, 2, 4, 6) => 11
# (1, 6)       =>  5
# ( )          => -1
# (6)          => -1 (because only one kid)


# [5,8,6,4]

# def foo(lol:list):

#     # dick = 0
#     # for i in lol:
#     #     if i > dick:
#     #         dick = i
#     if not lol or len(lol) == 1:
#         return -1 
    
#     can = 0

#     for num in lol:
#         can += max(lol) - num
    

#     return can

 
# print(foo([21, 84, 77, 43, 1, 88, 5, 68, 45, 32, 42, 78, 73, 87, 48, 74, 15, 95, 22, 20, 44, 77, 53, 21, 67, 68, 68, 94, 39, 95, 1, 73, 98, 48, 98, 47, 65, 83, 45, 71, 28, 94, 64, 93, 73, 59, 37, 22, 12, 35, 11, 81, 50, 80, 32, 68, 45, 70, 12, 77, 10, 47, 13, 98, 40, 5, 1, 12, 55, 6, 33, 54, 2, 35, 40, 47, 15, 82, 25, 51, 35, 98, 74, 3, 39, 53]))
# print(foo([1,2,4,6]))
# print(foo([7,7,7,7]))

                     #(34, 11, 6)

# def foo(legs_number, heads_number, horns_number):
    
#     if not heads_number or legs_number % 2:
#         return "Error"

#     cows = int(horns_number / 2)
    
#     heads_number -= cows
#     legs_number -= cows * 4


#     rabbits = int((legs_number - 2 * heads_number) / 2)
#     chicken = int(heads_number - rabbits)

#     return {"rabbits" : rabbits, "chickens" : chicken, "cows" : cows}


    #print(int(rabbits), int(chicken), int(cows))

    # rabbits = 

    # chickens = 

    # cows = horns_number / 2
# print(foo(34, 11, 6))
# print(foo(154, 42, 10))

# Input: 42145 Output: 54421

# Input: 145263 Output: 654321

# Input: 123456789 Output: 987654321

# def foo(lol):

#     dick = sorted(str(lol), reverse=True)

#     print(dick)
#     return None




# print(foo(12354))
# def foo(lol):
#     r = 0 
#     while lol > 0:
#         r *= 10
#         r += lol % 10
#         lol //= 10

#     return r

# print(foo(123456789))

# def lol(foo):

#     return int(''.join(sorted(str(foo),reverse=True)))


# print(lol(123412312))

# def lol(foo):

#     # arr = []
#     # for item in range(len(foo)):
#     #     arr.append(foo[0:item+1])
       
#     _ = str(foo)
#     return [_[0:i+1] for i in range(len(str(_)))]




# print(lol(420))
    



# def capitalize(s:str, l:list):

# #     new_str = ''
# #     for i in range(len(s)):
# #         if i in l:
# #             new_str+=s[i].capitalize()
# #         else:
# #             new_str+=s[i]
#     # return new_str

#     return ''.join(v.upper() if i in l else v for i, v in enumerate(s))




# print(capitalize("abcdef", [1,2,5]))



# def foo(m,n):
#     dick = []
#     for i in range(n):
#         lol = []

#         for j in range(m):
#             lol.append(i+1)

#         dick.append(lol)
#     return dick

# print(foo(5,8))




# def vaporcode(s:str):

#     # return '  '.join(i.upper() for i in s.replace(' ', ''))
#     return '  '.join(s.replace(' ', '').upper())


# print(vaporcode("Lets go to the movies"))

# def get_count(s):
#     # n = 0

#     # for i in s:
#     #     if i in 'aeiou':
#     #         n += 1

#     # return n


#     return (1 for i in s if i in "aeiouAEIOU")

# print(type(get_count('aeiou')))
# print(get_count('bcdfghjklmnpqrstvwxz y'))



# def foo(s):
#     a = '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     # sum = 0

#     # for i in s:
#     #     for k,v in enumerate(a):
#     #         if i == v:
#     #             sum += k+1 

#     # return sum
 
#     return sum(a.index(i) for i in s)




# print(foo('abc'))
# print(foo('attitude'))



# ;asldfja sl;dfj ;alsjdf
# l;asdfj;alsd asdfasdf asf asf 



#     # for i in s:
#     #     for k,v in enumerate(a):
#     #         if i == v:
#     #             sum += k+1 

#     # return sum
 
#     return sum(a.index(i) for i in s)











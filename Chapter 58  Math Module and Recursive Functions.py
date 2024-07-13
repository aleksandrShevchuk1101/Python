# import math

# print(math.e)
# print(math.pi)


# print(math.sqrt(10))
# print(math.sqrt(16))

# print(math.factorial(3))
# print(math.log10(1000))
# print(math.log2(8))


# print(math.floor(10.7))
# print(round(10.7))


import math

def calc_factorial(num: int):
    if type(num) is not int:
        raise TypeError("Number must be integer")
    
    if num <= 0:
        raise ValueError("Number must be positive")
    
    if num == 1:
        return 1
    
    return num * calc_factorial(num - 1)



print(calc_factorial(10.1))
print(math.factorial(10))



 
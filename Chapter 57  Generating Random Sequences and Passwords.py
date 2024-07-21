# import random

# # float
# print(random.random())
# print(random.uniform(10.5, 11.6))

# # int
# print(random.randint(100, 1000))

# # shuffle
# my_list = [1,2,3,4,5,6,7]
# print(my_list)
# random.shuffle(my_list)
# print(my_list)
# random.shuffle(my_list)
# print(my_list)

# # choice
# print(random.choice('Alex'))
# print(random.choice((4,5,6,7,1)))
# print(random.choice(['a', True, None]))



# print(random.choices([1,4,3,4,5], k = 3))
# print(random.choices('asdfasdfd', k = 5))
# print(''.join(random.choices('asdfasdfdasdfadf', k = 12)))


# # sample

# print(random.sample([1,2,3,4,5], k = 3))


# import secrets
# import string


# print(string.digits)
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.punctuation)



# all_chars = string.ascii_letters + string.digits + string.punctuation

# print(secrets.choice(all_chars))

# print(''.join(secrets.choice(all_chars) for i in range(10)))


# def generate_password(foo):

# print(' '.join(secrets.choice(all_chars)) for item in range(10))




# def generate_password(lenght):
#     all_chars = string.ascii_letters + string.digits + string.punctuation
#     password = ''

#     for i in range(lenght):
#         password += secrets.choice(all_chars)
#     return password


# print(generate_password(10))
# print(generate_password(100))


def generate_password(lenght):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join([secrets.choice(all_chars) for i in range(lenght)])
    return password


# print(generate_password(10))
# print(generate_password(20))
# print(generate_password(30))


# import secrets

# print(secrets.token_hex(8))
# print(secrets.token_hex(16))
# print(secrets.token_hex(24))



import secrets 
import string


counter = 0
def gen(lenght):
    global counter
    counter += 1

    digits = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(digits) for _ in range(lenght))
    return password

def gen_special_password(lenght: int):
    while True:
        p = gen(lenght) 
        if any(c.islower() for c in p) and any(c.isupper() for c in p) and any(c.isdigit() for c in p) and any(c in string.punctuation for c in p):
            break
    return p



print(gen_special_password(4))

print(counter)









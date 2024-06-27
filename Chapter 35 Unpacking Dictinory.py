# salary = 1  # int(input("Enter salary amount: "))
# quan = "hguj"  # int(input("Enter days quantity"))

# try:
#     salary_per_day = salary / quan
# except (TypeError, ZeroDivisionError) as e:
#     print(type(e))
#     print(e)
# # except ZeroDivisionError as z:
# #     print(type(z))
# #     print(z)
# else:
#     print("Lol")
# finally:
#     print("sfsdfasdf")



# # print(salary_per_day)


# try:
#     10 / 0
#     file = open("file.txt", "r")
# except FileNotFoundError as e:
#     print(e)
# except Exception as e:
#     print("asfdasdf")
# else:
#     print("File is ready for reading")
# finally:
#     if "file" in locals() and not file.closed:
#         file.close()
#         print("File was closed")    
#         print(file.closed)  
#     else:
#         print("asdfsadf") 



# def con_at_symbol(email):
#     return "@" in email

# def reg_user(email: str, age: int):
#     if not isinstance(email, str):
#         raise TypeError("Email must be a string")
    
#     if not isinstance(age, int):
#         raise TypeError("Age must be an int")

#     if not con_at_symbol(email):
#         raise ValueError("Invalid email")
    
#     print("User was registered")
#     return {'email':email, 'age': age }



# try:
#     registered_user = reg_user(5, 10)
#     print(registered_user)
# except (TypeError, ValueError) as e:
#     print(e)


def image_info(foo: dict):

    if not 'id' in foo or not 'image_title' in foo:
        raise TypeError("We don't have all keys") 

    return f"Image {foo['image_title']} has id {foo['id']}"


try:
    foo = image_info({'id' : 121324, 'image_title' : 'asdfasdl;fjas'})
except TypeError as t:
    print("We have an error")
else:
    print("Success")



foo1 = {'one': 'we', 'two': 2}

print('one' in foo1.keys())


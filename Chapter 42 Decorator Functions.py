
# def is_user_authenticated():
#     return True



# def check_user_auth(fn):
#     def wrapper(*args, **kwargs):
#         if is_user_authenticated():
#             print("User is authenticated")
#             return  fn(*args, **kwargs)
#         else:
#             raise Exception("User is not authenticated")
        
#     return wrapper


# @check_user_auth
# def do_sensitive_job():
#     # Perform action only if user is authenticated
#     print("Some sensitive job results")

# do_sensitive_job()



def log_funciton_call(fn):
    def wrapper(*args, **kwargs):
        print(f"Calling function {fn.__name__}")
        print(f"Fucntion arguments: {args}, {kwargs}")
        res = fn(*args, **kwargs)
        print(f"Result of the function is {res}")
        return res
    
    return wrapper


@log_funciton_call
def mult_numbers(a,b):
    return a * b


print(mult_numbers(10,2))

@log_funciton_call
def sum_numbers(a,b):
    return a + b


print(sum_numbers(10,5))


@log_funciton_call
def sum_numbers(a,b):
    return a + b 


print(sum_numbers(a = 10, b = 5))
# user_is_active = False

# foo = "User is active" if user_is_active else "User is not active"


# print(foo)


# def convert_status(actrive):
#     return "User is active" if actrive else "User is not active"

# print(convert_status(user_is_active))




# def check(is_memeber):
#     return 0.1 if is_memeber else 0.05
    

# customer_memeber = True

# per = check(customer_memeber)
# print(per)



# def process_data(data):
#     process_data = data if data is not None else []



#     return process_data


# rec = [1,2]

# foo = process_data(rec)

# print(foo)



def get_letter_grade(score):
    return 'A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'D' if score >= 60 else 'F' 



score = 15

print(get_letter_grade(score))
print(get_letter_grade(75))
print(get_letter_grade(60))
print(get_letter_grade(45))


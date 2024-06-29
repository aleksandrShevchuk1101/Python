# while True:
#     print("We are in the loop")


# user_name = ''

# while not user_name:
#     entered_usename = input("Please enter your username")
    
#     if len(entered_usename) > 3:
#         user_name = entered_usename
#     else:
#         print("Useraname is too short. Must be more than 3 characters!")

# print(f"Welcome {user_name}")

# import time

# seconds_qty = 5

# while seconds_qty > 0:
#     print(f"Timer: {seconds_qty}")
#     seconds_qty -= 1
#     time.sleep(1)

# print("Timer is up")


# selected_option = 1

# while selected_option not in range(1,4):
#     print("Menu:")
#     print("1. Start the game")
#     print("2. Load saved game")
#     print("3. Quit")
#     try:

#         selected_option = int(input("Please enter the choise"))
#     except ValueError as e:
#         print(e)
#         print("Try to select option once again")

# if selected_option == 1:
#     print("Staring the game...")

# if selected_option == 2:
#     print("Loading saved game")

# if selected_option == 3:
#     print("Quiting")

# user_password = 'admin123'
# password = ''

# while password != user_password:
#     print("Enter 'quit in order to exit from login")
#     password = input("Please enter your password: ")

#     if password == 'quit':
#         print("Quiting...")
#         break

#     if password == user_password:
#         print("Login successful!")
#     else:
#         print("Login failed")


# my_list = [10, 5, 2, 100, 35]

# for num in my_list:
#     if num == 2:
#         break
#     print(num)


# current_usernames = ['alex777', 'asdfadsf', 'qwer']



# while True:
#     username = input("Please enter disired username: ")

#     if username in current_usernames:
#         print("User name is already taken. Try again")
#         continue
    
#     current_usernames.append(username)
#     break

# print("User registratioin complete.")
# print(current_usernames)


# while True:
#     num_1 = input("Enter first number")
#     num_2 = input("Enter second number")

#     print(f"The result is {num_1 / num_2}")
#     res = input("Do you wanna to continue? Yes or no")

#     if res == 'no':
#         break
#     elif res == 'yes':
#         continue



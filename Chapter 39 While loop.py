#while Condition:

#while False
#While True


""" i = 10

while i < 50:
    print(i)
    i += 10


while True:
    print("Infinite loop")


while True:
    answer=input("Enter yes or no: ")
    if answer == 'no':
        break """


""" import random

random_numer = random.randint(1,5)

while True:
    num = int(input("Guess the number from 1 to 5"))

    if num != random_numer:
        print("Try again")
        continue


    print("You gussed the number. Congratulations!!!")
    break """

""" username = ''  

while not username:
    user_name = input("Please enter your user name: ")
    if len(user_name) >= 3:
        username=user_name
    else:
        print("User name is too short, please enter long one")

print(f"Welcome, {username}") """


""" import time

seconds_qty = 10

while seconds_qty > 0:
    print(f"The ramaining time is {seconds_qty} seconds")
    seconds_qty -= 1
    time.sleep(1)

print("The time is up!!!") """


""" selected_option = 2

while selected_option not in range(1,4):
    print("Menu: ")
    print("1. Start the game")
    print("2. Load saved game")
    print("3. Quit")

    #selected_option = "sadfasdfas"
    
    try:
        #selected_option = int(input("Please enter your choice (1-3): "))
        selected_option = int(selected_option)
        
    except ValueError as e:
        print(e)
        print("Try to select option one agene")
        
    #break """


""" if selected_option == 1:
    print(f"Your choise the {selected_option} - Starting the game")
elif selected_option == 2:
    print(f"Your choise the {selected_option} - Saving the game")
else:
    print(f"Your choise the {selected_option} - Quiting") """


""" my_str = "Starting the game" if selected_option == 1 else "Saving the game" if  selected_option == 2 else "Quiting"

print(my_str) """


""" user_password = 'admin123'
password = 'quit'

while password != user_password:
    print("Enter quit in order to exit from login")
    #password = input("Please enter your password") 
    if password == 'quit':
        print("Quitting...")
        break

if password == user_password:
    print("Login successful")
else:
    print("Login is failed") """

""" current_username = ['bogdan123', 'bob1', 'alice75']
foo = False

while True: 
    user_name = 'bob1' #input("Please enter desired username: ")

    if user_name in current_username and not foo:
        print("User name is already taken. Try again")
        foo = True
        continue

    current_username.append(user_name)
    break

print("User registration complete.")
print(current_username) """



#Task

first_number = 1
second_number = 35

while True:
    print("Enter first number ")
    print("Enter second number ")

    print(f"Ther result id {first_number/second_number}")

    print("Do you want to continue: ")

    foo = 'false'

    if foo == 'yes':
        continue

    break


   
















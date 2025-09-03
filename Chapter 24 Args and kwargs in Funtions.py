

# def sort_nums(*args):
#     # print(args)
#     # print(type(args))
#     # args.append(10)
#     for item in args:
#         print(item)

# def foo(*item):
#     return sorted(item)

# sorted_nums = foo(10, 3, 15, 246) 
# print(sorted_nums)


# def get_posts_info(name, posts_qty):
#     info = f"{name} wrote {posts_qty} posts"
#     return info

# string = get_posts_info(name = "Alex", posts_qty = 25)

# print(string)


# def get_posts_info(**person):
#     print(person)
#     print(type(person))
    
#     string = ( f"{person['name']} is {person['age']}"
#             f" lives in {person['city']}"
#     )
#     return string


# print(get_posts_info(name = "Alex", age = 25, city = "Rotterdam"))



# def comments_info(**args):
#     print(f"{args['qty']} comments where posted on {args['day']}")

# comments_info(qty = 50,day = "Monday")


# def product_price_info(**product):
#     print(f"The {product['title']} costs {product['price']}")


# product_price_info(title = "Milk", price = 1)

# def merge_lists_to_dict(first_list, second_list):
#     print(list(zip(first_list, second_list)))
          

# merge_lists_to_dict([1,243,4,5], ["sdf", 'adfadsf'])

def send_email(to, subject, *args, **kwargs):
    print(f"Sending an email to: {to} ...")
    print(f"Email subject: {subject}")

    if args:
        print("Additional recipients:")
        for item in args:
            print(item)
    
    if kwargs:
        print("Additonal detail for the email:")
        for key in kwargs:
            print(f"{key}: {kwargs[key]}")

    print(list(kwargs))


#send_email('test@test.com', "Hello there!", 'other@test.com', 'leito1101@gmail.com', bcc = "leito1101@gmail.com", img = 'test.png')

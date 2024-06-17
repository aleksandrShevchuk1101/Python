

# my_bike = {'brand' : 'Custom',
#             'price' : 3000
#             }


# print(my_bike)
# print(type(my_bike))
# print(len(my_bike))

# my_bike["max_speed"] = 50

# print(my_bike)


# other_bike = {
#     'price' : 2000,
#     'brand' : 'Custom'}

# print(my_bike == other_bike)

# foo = list(my_bike.keys())

# print(type(foo))

# print(my_bike.items())

# brand = "Ducati"
# bike_price = 25000
# engine_volume = 1.2

# my_motorbike = {
#     'brand': brand,
#     "price": bike_price,
#     "volume": engine_volume
# }

# print(my_motorbike)


# my_string = 'abcd'
# my_dict = dict(my_string)


my_dict = {}

for item in range(3):
    key = input("Type the key")
    value = input("Type the value")

    my_dict[key] = value

print(my_dict)


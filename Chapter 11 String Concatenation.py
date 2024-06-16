
# hello = "Hello"
# world = "World"

# greetint = f"{hello} {world}"

# print(greetint)


my_name = "Aleksandr"
my_hobby = "running"

time = [1,2]

# info = my_name + " likes " + my_hobby + " at " + str(time) + " o'clock"

# print(info)

info = f"{my_name} likes {my_hobby} at {time} o'clock"
print(info)

info = "{} likes {} at {} o'clock".format(my_name, my_hobby, time)
print(info)


info = "%s likes %s at %s o'clock" % (my_name, my_hobby, time)
print(info) 
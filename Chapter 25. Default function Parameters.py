
from datetime import date

def foo(value, multiplier=1):
    return value*multiplier


print(foo(4,4))
print(foo(4,1))

def get_weekday():
    return date.today().strftime('%A')


def create_new_post(post, weekday = get_weekday()):
    post_copy = post.copy();
    post_copy['date'] = weekday
    return post_copy

initinal_dict = {
    'id' : 243,
    'author' : 'Bogdan'
}

foo = create_new_post(initinal_dict, "lol")
print(foo)

foo = create_new_post(initinal_dict)
print(foo)
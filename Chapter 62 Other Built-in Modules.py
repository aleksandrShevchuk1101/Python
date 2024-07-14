from array import array
import sys


my_array = array('i', [10,4,3,7,2,5])
# print(my_array)
# print(type(my_array))
# print(dir(my_array))

# print(my_array[2])
# my_array.append(20)
# print(my_array)
# # print(my_array[10.2])
# my_array.append(True)
# print(my_array)
# print(isinstance(True, bool))
# print(isinstance(True, int))
# print(int.__subclasses__())
# my_array.pop(0)
# print(my_array)

# with open('my_array.bin','wb') as file:
#     my_array.tofile(file)


# new_array = array('i')
# with open('my_array.bin','rb') as file:
#     new_array.fromfile(file, 3)

# print(new_array)



# print(sys.argv)

import webbrowser


def search_on_search_engine(query, search_engine):
    search_engines = {
            'google': 'https://www.google.com/search?q={}',
            'yahoo': 'https://search.yahoo.com/search?p={}',
            'bing': 'https://www.bing.com/search?q={}',
            'ya': 'https://yandex.kz/search/?text={}'
    }

    if search_engine not in search_engines:
        print("Unsupported search engine:", search_engine)
        return 
    
    search_url = search_engines[search_engine].format(query)

    webbrowser.open(search_url)



search_on_search_engine("Python programming", 'ya')



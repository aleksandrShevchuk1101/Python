

from copy import deepcopy


info = {
    'name': 'Alex',
    'is_instructor': True,
    'reviews': []
}

info_deepcopy = deepcopy(info)

info_deepcopy['reviews'].append("Great course")

print(info)
print(info_deepcopy)

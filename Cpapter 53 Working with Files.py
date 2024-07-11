# from pathlib import Path

# # print(Path.cwd())


# for f in Path('.').iterdir():
#     print(f)


# import os

# directory_path = 'my_test_directory'

# # Check if directory exists
# if not os.path.exists(directory_path):
#     os.mkdir(directory_path)
#     print("Directory was created",directory_path )
# else:
#     print("Directory exist", directory_path)


# # Creating path to the file
# file_path = os.path.join(directory_path, 'my_file.txt')
# print("File path: ", file_path)

# # Getting parent directory
# parent_dir = os.path.dirname(file_path)
# print("Parent name is ", parent_dir)

# Checking if the file is file path or dir path

# is_file = os.path.isfile(file_path)
# is_dir = os.path.isdir(directory_path)

# print(is_file)
# print(is_dir)


# # Listing files in the directory
# dir_files = os.listdir(directory_path)

# print(dir_files)

# # Removing directory

# if os.path.exists(directory_path):
#     dir_files = os.listdir(directory_path)
#     for file in dir_files:
#         os.remove(os.path.join(directory_path, file))


#     os.rmdir(directory_path)
#     print("Deleted")


from pathlib import Path

directory_path = Path("my_test_directory")
print(type(directory_path))


if not directory_path.exists():
    # Create directory
    directory_path.mkdir()
    print("Directory was created: ", directory_path)
else:
    print("Directory already exists")


file_path = directory_path / 'my_file.txt'
# file_path = directory_path.joinpath('my_file.txt')
# print("File path is: ", file_path)

parent_dir = file_path.parent
print(parent_dir)


is_file = file_path.is_file()
is_dir = directory_path.is_dir()

print(is_file)
print(is_dir)


files = [item.name for item in directory_path.iterdir() if item.is_file()]
print(files)


if directory_path.exists():
    files = [file for file in directory_path.iterdir()]
    for file in files:
        file.unlink()
        
    directory_path.rmdir()

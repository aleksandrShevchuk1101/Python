from zipfile import ZipFile
from pathlib import Path

files_dir = Path('my-file')

if not files_dir.exists():
    files_dir.mkdir()

zip_archive = Path('my-files.zip')

if zip_archive.exists(): 
    zip_archive.unlink()

with open('my-file/first.txt','w') as file:
    file.write("This is first line\n")

with open('my-file/second.txt', 'w') as file:
    file.write("This is second line\n")

with ZipFile('my-files.zip', mode = 'w') as zip_file:
    for file in files_dir.iterdir():
        zip_file.write(file)


with ZipFile('my-files.zip') as zip_file:
    # print(zip_file)
    # print(type(zip_file))
    # print(zip_file.infolist())
    # zip_file.extractall('unzipped-my-files')
    zip_file.extract("my-file/first.txt", "individual-files")




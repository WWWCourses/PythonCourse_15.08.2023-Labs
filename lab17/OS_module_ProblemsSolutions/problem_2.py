# Да се напише програма, която да намери всички всички файлове и директории в дадена директория. Програмата да създаде списък само от директориите, списък само от файловете и списък от директории и файлове.

# os.listdir(path)

# os.path.isdir(path) –  Връща True ако дадената директория съществува.

# os.path.join(path, *paths) – свързва повече от една директории, като образува един общ път.


import os

dir_name = 'test_data'
dir_path = os.path.join(os.getcwd(),dir_name)


dir_content = os.listdir(dir_path)
print(dir_content)

directories = []
files = []


# print( os.path.isdir('dir_1'))

# # ### using loops
for entry in dir_content:
    print(entry)
    entry_path = os.path.join(dir_path,entry)

    if os.path.isdir(entry_path):
        directories.append(entry)
    else:
        files.append(entry)

print(f'Files: {files}')
print(f'Directories: {directories}')

# print('~'*80)

# ### using list comprehensions
# directories = [entry for entry in dir_content if os.path.isdir(os.path.join(dir_path,entry))]

# files = [entry for entry in dir_content if not os.path.isdir(os.path.join(dir_path,entry))]

# print(f'Files: {files}')
# print(f'Directories: {directories}')

# print('~'*80)

# ### using filter:
# directories = filter(
#     lambda entry:os.path.isdir(os.path.join(dir_path,entry)),
#     dir_content)
# files = filter(
#     lambda entry:not os.path.isdir(os.path.join(dir_path,entry)), dir_content)

# print(f'Files: {list(files)}')
# print(f'Directories: {list(directories)}')




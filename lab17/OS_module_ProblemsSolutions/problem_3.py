# Да се напише програма, която да сканира определена директория и да намери всички поддиректории и файлове в нея.

# os.scandir(path=‘.’) – Връща итератор на os.DirEntry обекти съществуващи в посочената от path директория. Използвайте scandir() вместо listdir(), това ще увеличи бързодействието на вашата програма.

# os.is_dir(*, follow_symlinks=True) –  Връща True ако подаденият път е директория или symbolic link към директория. Връща False ако директорията не съществува или symbolic link сочи към друга директория. Ако вторият параметър follow_symlinks е False , връща True само ако пътя е директория (без да има свързани symbolic links). Връща False ако не съществува. Функцията кешира резултатите като ги съхранява в os.DirEntry обект. Тази функция може да хвърли грешки като OSError и PermissionError, но FileNotFoundError се хваща като грешка и не се хвърля допълнително.

# os.is_file(*, follow_symlinks=True) – Връща True ако въведеният път е файл или symbolic link към файл. Връща False ако файлът не съществува или няма линк към друг файл.

import os


dir_name = 'test_data'
dir_path = os.path.join(os.getcwd(),dir_name)
# note, that we convert generator to list, as after the first list comprehension bellow the genereator will be exausted and the second one would not yield values
dir_content = list(os.scandir(dir_path))

# print(dir_content)

files = [entry.name for entry in dir_content if entry.is_file()]
directories = [entry.name for entry in dir_content if entry.is_dir()]

print(f'Files: {files}')
print(f'Directories: {directories}')

print('~'*80)

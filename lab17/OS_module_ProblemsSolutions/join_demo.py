import os

path1 = '/dir1/dir2/'
file_name = 'file1.txt'

file_path = path1 + '/' + file_name
print(file_path)

file_path = os.path.join(path1,file_name)
print(file_path)

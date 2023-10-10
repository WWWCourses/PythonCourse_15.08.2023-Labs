import os

# path_in_windows = 'C:\\Users\\User\\Desktop\\pythoncourse\\homework\\hw_1.py'
# print(path_in_windows)

# # posix == 'linux', 'MakOS'
# path_in_posix = '/home/ada/Desktop/pythoncourse/homework/hw_1.py'



path1 = 'C:\\users\\ada'
# path1 = 'dir1'
path2 = 'test'

print(os.path.join(path1,path2))


print(os.path.basename('/users/ada/test.txt'))
print(os.path.dirname('/users/ada/test.txt'))
print(os.path.split('/users/ada/test.txt'))

# print(os.path.splitext('/users/ada/test.txt'))
print(os.path.exists('/users/ada/test.txt'))
print(os.path.exists('/home/nemsys'))
# print(os.path.isdir('/home/nemsys'))
# print(os.path.isfile('/home/nemsys'))

print(os.path.abspath('./os.path_demos.py'))
print(os.path.getsize(os.path.abspath('./os.path_demos.py')))
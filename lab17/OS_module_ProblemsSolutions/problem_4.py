# os.path.islink() – Връща True  ако обекта е symbolic link (дори и да е счупен).

import os

cwd = os.getcwd()

# create symlink 'dir_1_symplink' in dir_3 pointing to dir_1:
try:
	os.symlink(
		os.path.join(cwd,'test_data','dir_1'),
		os.path.join(cwd,'test_data','dir_3','dir_1_symplink')
	)
except FileExistsError as e:
	print(e)


content = os.scandir(os.path.join(cwd,'test_data','dir_3'))
for entry in content:
	print(os.path.islink(entry))
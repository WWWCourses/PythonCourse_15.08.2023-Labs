# Да се напише Python програма, която да покаже името на операционната система, текущата директория, принтира файловете от директорията и да хвърли грешка в случай, че не съществува името на файла или пътя.

# import os
# os.name – връща името на операционната система

# os.getcwd() – връща текущата директория като стринг

# os.listdir(path=‘.’)  връща списък на всички имена съдържащи се в дадена директория, като параметърът path оказва, името на директорията.

import os

# print(f'OS: {os.name}')

# CWD = Current Working Directory
cwd = os.getcwd()
print(f'CWD: {cwd}')

# ### using listdir()

entries = os.listdir(path=cwd)
print(f'Listdir Entries')
for e in entries:
	print(e)

# print('~' * 80)

# ### using Path.glob()
from pathlib import Path

entries = Path(cwd).glob('*.py')
for e in entries:
	print(e)

# print('~' * 80)






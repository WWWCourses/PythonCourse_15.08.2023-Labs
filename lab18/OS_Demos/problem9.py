# Напишете програма, която да обходи зададена директория и да принтира всичко което се съдържа в нея.

# os.walk(top, topdown=True, onerror=None, followlinks=False) – генерира имената на всичко което се съдържа е дадена директория, като използва техники като отгоре-надолу или отдолу-нагоре.

# оs.path.split() – разделя това което му се подава и полученият резултат се представя като тупъл.
# #

import os

path = './test/'
# print(os.listdir(path))
# print(os.walk(path))

# for entry in os.walk(path, topdown=False):
# 	print(entry)
# 	# if entry.isfile



path = os.path.join('/user/test/', 'a///', 'b')
print(path)

print( os.path.split(path))
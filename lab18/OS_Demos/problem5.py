import os
from datetime import datetime


stat = os.stat(path='../tmp.py')
ctime_human = datetime.fromtimestamp(stat.st_ctime)
print(ctime_human)

print(f'size: {stat.st_size}')


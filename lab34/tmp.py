import re

rx = re.compile(r'[a-b](?i)[a-b]')
print(rx.search('aA'))
import re
# --------------------- Compile regex object from string --------------------- #
# test_string = '123ABC'
# regex = re.compile(r'[0-9]+[a-z]', flags=re.I)

# m1 = regex.search(test_string,2)
# m2 = re.search(r'[0-9]+[a-z]', test_string[2:], flags=re.I)

# print(m1)
# print(m2)

# ------------------ Best Practice to use precompiled regex ------------------ #
# ## In a loop:
# strings = [
# 	'123ABC',
# 	'123abc'
# ]

# ### not so efficient
# for string in strings:
# 	m = re.search(
# 		pattern=r'[a-z]+',
# 		string = string,
# 		flags=re.I
# 	)
# 	print(m)

# ### more efficient:
# rg = re.compile(r'[a-z]+',flags=re.I)
# for string in strings:
# 	m = rg.search(
# 		string = string
# 	)
# 	print(m)

# ---------------------------------- match() --------------------------------- #
# strings = [
# 	'123ABC',
# 	'123abc'
# ]
# rg = re.compile(r'a', flags=re.I)
# for string in strings:
# 	m = rg.match(string)
# 	print(m)


### Example
# Valid password: at least 3 letters, case-insensitive
# passwords = [
# 	'abc', 		# ok
# 	'Xabc', 	# ok
# 	'Xa', 		# not ok
# 	'1abc', 	# not ok
# 	'a2bcaf', 	# not ok
# 	'abc1', 	# not ok
# 	'abcdfdsj1', # not ok
# ]

# rg = re.compile(r'[a-zA-Z]{3,}')
# for pwd in passwords:
# 	m = rg.fullmatch(pwd)
# 	if m:
# 		print(f'{pwd} is valid!')

# --------------------------------- findall() -------------------------------- #
# test_string = '11a22b33c'
# regex_str = r'[0-9]+?'
# rg = re.compile(regex_str)

# print( rg.findall(test_string) ) #match='11a'

# ---------------------------------- split() --------------------------------- #
### Example: count words:
## words are separated by: ' ','.',','
# test_string = 'If the whole,string matches this regular expression, return a corresponding Match.Return None if the string does not match the pattern; note that this is different from a zero-length match.'
# rg = re.compile(r'[ .,]')

# words = rg.split(test_string)
# print(words)

# ----------------------------- sub() and subn() ----------------------------- #
### Example: Remove all digits from text
# test_string = 'abcb 2jjh24kj 45454k !'
# rg = re.compile(r'[0-9]')
# replaced_string = rg.sub('',test_string)
# print(replaced_string)

# (replaced_string,repl_count) = rg.subn('', test_string)
# print(replaced_string,repl_count)

# --------------------------------- escape() --------------------------------- #
### Example: escape Windows path
### C:\pesho\programs\python.exe

# path = 'C:\\pesho\\progr`ams\\test.exe'
# escaped_path = re.escape(path)
# print(path)
# print(escaped_path)








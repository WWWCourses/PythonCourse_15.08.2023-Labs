import re
# ----------------------------- Character Classes ---------------------------- #

### .
# test_str = '''ab$~
# 1
# '''
# rg = re.compile(r'.+1', re.DOTALL)
# m = rg.search(test_str)
# print(m)

### \w = [0-9a-zA-Z_]

# ### Example: match valid Python variables names
# test_strings = [
# 	'1a',  	  # not ok
# 	'a-1',    # not ok
# 	'ab!',    # not ok
# 	'a_1',    # ok
# 	'_1',     # ok
# 	'__1',    # ok
# 	'__a',    # ok
# 	'a_b_c',  # ok
# ]

# rg = re.compile(r'[_a-zA-Z]\w+')
# for test_str in test_strings:
# 	m = rg.fullmatch(test_str)
# 	if m:
# 		print(f'{test_str} is ok')


### Example: get list of words:
# test_string = 'If the whole,string matches this regular expression, return a corresponding Match1.Return None if the str_ing does not match the pattern; note that this is different from a zero-length match.'

# rg = re.compile(r'\w+')
# words = rg.findall(test_string)
# print(words)

# ----------------------------------- Flags ---------------------------------- #
#### re.VERBOSE|re.X

rg_str = r'''
[\d-] 		# digit or -
\w+ 		# sequnese of 1 or more [0-9a-zA-Z_]
'''
test = '1-abc'

rg = re.compile(rg_str, flags=re.X)
print(rg.search(test))


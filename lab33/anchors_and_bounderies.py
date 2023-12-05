import re
from string import octdigits

# ---------------------------------- Anchors --------------------------------- #
# test_strings = [
# 	'abc',
# 	'cat',  # ok
# 	'acat',
# 	'caterpilar'
# ]

# rg = re.compile(r'^cat$')
# for test_str in test_strings:
# 	m = rg.search(test_str)
# 	if(m):
# 		print(f'{test_str} ok')


# --------------------------------- Boundary --------------------------------- #
# \b => [a-zA-Z0-9_][^a-zA-Z0-9_^$] ||[^a-zA-Z0-9_][a-zA-Z0-9_]
# test_strings = [
# 	'', 		# no
#   	'a',		# yes
#   	'@',		# no
#   	'@a',		# yes
#   	'aa', 		# yes
#   	'a!',		# yes
#   	'a,a',		# yes
# ]


# rg = re.compile(r'\b')
# for test_str in test_strings:
# 	m = rg.findall(test_str)
# 	if(m):
# 		print(f'{test_str} : {m}')

# -------------------------------- Alternation ------------------------------- #
# test_strings = [
# 	"abc",
# 	"cat",  # ok
# 	"acat",
# 	"caterpilar",
# 	"dog", # ok
# 	"dogger",
# 	"adog",
# 	"cat!"  # no
# ]


# rg = re.compile(r'^(cat|dog)$')
# for test_str in test_strings:
# 	m = rg.findall(test_str)
# 	if(m):
# 		print(f'{test_str} : {m}')


# ---------------------------- Capturing/Grouping ---------------------------- #
# test_strings = [
# 	"ivan: 2773", #ok, $1=ivan, $2=2773
# 	"pesho: 23",  # ok
# 	"#pesho: 23",
# 	"pesho 23",
# 	"pesho23",
# ]
# # TASK: get all users and their balance, if they follow: '<name>:<balance>'

# data = {}
# rg = re.compile(r'^([a-z]+):\s(\d+)$',re.IGNORECASE)
# for test_str in test_strings:
# 	m = rg.search(test_str)
# 	if(m):
# 		# print(m.groups()]
# 		# print(m.group(1), m.group(2))
# 		# print(m[1], m[2])
# 		data[m.group(1)]=m.group(2)

# print(data)

# TASK: get list of "words":
# a word is a string separated by spaces
# text = """
# kjjkdjfd madam kjjkdjfd
# jksjdk@abc@345jk 1abc1 fdskj
# !ok! @abc@
# a434#)43a
# """
# words = re.compile(r'\s').split(text)
# words = [el for el in words if el!='']

# print(words)


# ### TASK: find all words which starts and end with same symbol
text = """
kjjkdjfd madam kjjkdjfd
jksjdk@abc@345jk 1abc1 fdskj
!ok! @abc@
a434#)43a
"""

words = re.compile(r'\s').split(text)
words = [el for el in words if el!='']
print(words)


rg = re.compile(r'(.).*\1')

matched_words = []

# matched_words = [w for w in words if rg.search(text)]
# print(matched_words)
matched_words = list(filter(lambda word: rg.search(word), words))
print(matched_words)

# jjkdjfd madam kjj
# rg = re.compile(r'\b(\S)\w+\1\b')














import re

# ------------------------------ match vs search ----------------------------- #
test_str = '1221abcttyi'
patter_str = r'abc'

### search:
# using method on re module
res = re.search(patter_str, test_str)
print(res)

# using method on regex object
regex_obj = re.compile(patter_str)
regex_obj.search(test_str,0,4)
print(res)

regex_obj.search(test_str[0:4])
print(res)


### match:
# using method on re module
res = re.match(patter_str, test_str)
print(res)

# using method on regex object
regex_obj = re.compile(patter_str)
regex_obj.match(test_str,0,4)
print(res)

regex_obj.match(test_str[0:4])
print(res)


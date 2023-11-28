import re


# Valid phone number:
# 1. at least 8 consequent digits
test_strings = [
  'maria, asen123, pesho'
]

# '','a','aa',...'aa.....aaa'

pattern = r'[a-z]+'


for test_string in test_strings:
  res =  re.findall(pattern, test_string)
  if res:
    print(f"Pattern /{pattern}/ MATCHED string {res}!")
  else:
    print(f"Pattern /{pattern}/ DID NOT MATCHED string {test_string}!")

import re

# get html :
with open('./htmls/index.html') as f:
    content = f.read()

# print(content)

# get UL element content:

rg = re.compile(r'<ul id="menu">(.+?)</ul>', re.DOTALL)

m = rg.search(content)
if m:
    items = m.groups(1)


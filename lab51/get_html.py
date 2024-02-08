import requests

URL = 'https://www.jarcomputers.com/Laptopi_cat_2.html?ref=c_1'

def save_to_file(content, filename="./htmls/cotent.html"):
    with open(filename, 'w') as f:
        f.write(content)

r = requests.get(URL)
if r.ok:
    content = r.text
    save_to_file(filename="./htmls/Laptopi_cat_2.html", content=content)

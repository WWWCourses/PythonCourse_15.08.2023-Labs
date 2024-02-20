import re

def extract_screen_size(text:str)->float:
    regex = re.compile(r'^\s*([\d.]+)')
    m = regex.match(text)
    if m:
        size_str = m.group(1)
        return size_str'



text = '15.6" (39.62 cm) '
scren_size = extract_screen_size(text)
print(scren_size)
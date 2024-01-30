# ---------------------------------- basics ---------------------------------- #
# import pprint

# pp = pprint.PrettyPrinter(indent=4, depth=2)

# import requests

# url = 'http://127.0.0.1:8080/index.html'

# response = requests.get(url)

# pp.pprint(f'request headers: {response.request.headers}')
# # pp.pprint(f'response.headers: {response.headers}')
# # pp.pprint(f'response.encoding: {response.encoding}')
# pp.pprint(f'response.status_code: {response.status_code}')
# # pp.pprint(f'response.text: {response.text}')


# if response.ok:
#     content = response.text
#     print(f'Parse conent')


# ------------------------------ Get Prices Demo ----------------------------- #
# import requests

# header = {
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
#     'sec-ch-ua-platform': "Linux"
# }

# url = "http://127.0.0.1:8080/pages/prices.html"

# response = requests.get(url, headers=header)
# print(f'request headers: {response.request.headers}')
# if response.ok:
#     content = response.text
#     print(f'content: {content}')


# ----------------------------- Another Get Demo ----------------------------- #
# import requests

# def save_to_file(conent, filename='./data/softwareacademy.html'):
#     with open(filename, 'w') as f:
#         f.write(conent)

# url = 'https://softwareacademy.bg/'

# r = requests.get(url)

# if r.ok:
#     content = r.text
#     print(f'encoding: {r.encoding}')
#     # save_to_file(content)


# ------------------------- Get from SimpleHTTPServer ------------------------ #
import requests

url = 'http://localhost:8080'

r = requests.get(url)

if r.ok:
    content = r.text
    # print(f'encoding: {r.encoding}')
    # print(f'respone header: {r.headers}')
    print(content)
import bs4

# ------------------------------- Get elements ------------------------------- #
# html = """
# <body>
#     <h1>Heading 1</h1>
#     <p>Some text</p>
#     <a href="/post/123324">News 1</a>
#     <a href="/post/123325">News 2</a>
#     <span class="date red">13.02.24</span>
#     <span aria-label="IMDb rating: 6.0">other</span>
#     <span aria-label="test">other</span>
# </body>
# """


# soup = bs4.BeautifulSoup(html, 'html.parser')
# # print(soup.prettify())


# # get span elements:
# # print( soup.find('span'))
# # print( soup.find_all('span'))

# date = soup.find(class_= "red")
# print(date)

# a =  soup.find(href="/post/123324")
# print(a)
# span_raiting = soup.find('span', attrs={"aria-label":"IMDb rating: 6.0"} )
# print(span_raiting)

# --------------------------- Get text from element -------------------------- #

# html = """
# <body>
#     <div class="menu">
#         cccccc
#         <h2>aaaaaaaaaaaaa</h2>
#         <a href="#">bbbbbbbb</a>
#     </div>
# </body>
# """

# soup = bs4.BeautifulSoup(html, "html.parser")

# div_menu = soup.select_one('div.menu')
# if div_menu:
#     print(div_menu.text)



# ---------------------------- Navigating the tree --------------------------- #
with open('./page.html', 'r') as f:
    html = f.read()

soup = bs4.BeautifulSoup(html, "html.parser")

data = []
links = soup.select('a[href^="/products"]')
for link in links:
    title = link.parent.find('h3').text
    href = link['href']
    data.append((title, href))

print(data)













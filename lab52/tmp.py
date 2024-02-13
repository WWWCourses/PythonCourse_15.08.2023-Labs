import bs4
from matplotlib.pyplot import title

html = """
<body>
    <ul class="page-1">
        <li>
            <div>...</div>
            <div>
                <div>lllll</div>
                <div class="card-title">
                    <span>
                    Title1
                    </span>
                </div>
            </div>
        </li>
        <li>
            <div>...</div>
            <div>
                <div>lllll</div>
                <div class="card-title">
                    <span>
                    itle2</span>
                </div>
            </div>
        </li>
    </ul>
</body>
"""

soup = bs4.BeautifulSoup(html, 'html.parser')

ul = soup.find(class_="page-1")

if ul:
    li_items = ul.find_all('li')
else:
    raise Exception('Can not find li')

print( len(li_items) )


span_titles = ul.select("li div.card-title>span")

titles = [span.text.strip() for span in list(span_titles)]
print(titles)

# for li in li_items:
#     div_title = li.find('div', class_="card-title")
#     if div_title:
#         print(list(div_title.children)[1])
#         # title = div_title.children

    # titles.append(div_title)

# print(titles)





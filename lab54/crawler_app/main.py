from crawler_app.crawler import Crawler
from crawler_app.scraper import Scraper

if __name__=='__main__':
    url = 'https://www.jarcomputers.com/Laptopi_cat_2.html?ref=c_1'

    crawler = Crawler(url)
    html = crawler.get_html()

    scraper = Scraper(html)
    scraper.get_products()

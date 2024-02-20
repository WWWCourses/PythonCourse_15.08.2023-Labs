import logging

from bs4 import BeautifulSoup

format_str = '%(name)s:%(levelname)s:%(message)s'
logging.basicConfig(format=format_str, level=logging.DEBUG)
logger = logging.getLogger('scraper')

class Scraper:
    def __init__(self, html) -> None:
        self.soup = BeautifulSoup(html, "html.parser")

    def get_products_urls(self):
        products_urls = []

        logger.info('Start scraping data')
        products_selector = "#product_list .sProduct .s2"

        products = self.soup.select(products_selector)
        logger.debug('PRODUCTS: %s', products)
        for product in products:
            logger.debug('PRODUCT: %s', product)
            # get brand
            brand = product.select_one('.list_brand brand').text.strip()

            if brand == 'Lenovo':
                # get product link:
                a = product.select_one('.long_title description>a')
                href = a['href']
                products_urls.append(href)

        return products_urls



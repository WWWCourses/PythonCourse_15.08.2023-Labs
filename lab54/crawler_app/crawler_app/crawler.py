""" crawler module"""

import requests
import logging

format_str = '%(name)s:%(levelname)s:%(message)s'
logging.basicConfig(format=format_str, level=logging.INFO)
logger = logging.getLogger('crawler')



class Crawler:
    """
        https://www.jarcomputers.com/laptopi-cat-2.html?ref=c_1&page=1
    """
    def __init__(self, url) -> None:
        self.page = 1
        self.url = url
        self.target_url = f'{self.url}&page={self.page}'


    def get_html(self)->str:
        """_summary_
        """
        response = requests.get(self.target_url, timeout=8)
        # response.raise_for_status()

        if response.ok:
            html = response.text
            logger.debug('HTML: %s', html)
            logger.info('HTML is ready!')
            return html
        else:
            return ""


if __name__=='__main__':
    url = 'https://www.jarcomputers.com/Laptopi_cat_2.html?ref=c_1'

    crawler = Crawler(url)
    crawler.get_html()
import requests
import bs4
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def get_html(url):
    """Retrieves the HTML content of a given URL, handling errors appropriately."""

    # set user-agent
    user_agent = "A scrapper for learning"
    headers = {"User-Agent": user_agent}

    # perform GET request
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        response.encoding = "utf-8"
        return response.text

    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to retrieve HTML from {url}: {e}")
        raise  # re-raise the exception to be handled by the caller


def get_data(html):
    soup = bs4.BeautifulSoup(html, "html.parser")
    countries = soup.select('#countries div.country')
    for country in countries:
        title = country.select_one('h3').text.strip()
        print(title)


if __name__=="__main__":
    url = 'https://www.scrapethissite.com/pages/simple/'
    html = ''

    try:
        html = get_html(url)
    except Exception as e:
        logger.error(f"An error occurred: {e}")

    # print(html)
    get_data(html)
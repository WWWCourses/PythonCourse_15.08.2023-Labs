from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome and Selenium
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("http://example.com/client-rendered-page")

# Wait for JavaScript to render
driver.implicitly_wait(10)  # Adjust the wait time as necessary

# Get the rendered html content
html = driver.page_source
print(html)

driver.quit()

# You can then parse html content with BeautifulSoup or another parser

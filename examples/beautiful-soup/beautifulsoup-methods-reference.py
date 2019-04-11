from bs4 import BeautifulSoup
import requests
response = requests.get(
    'http://dataquestio.github.io/web-scraping-pages/simple.html')

# HTML content using content property
# print(response.content)

# Parsing with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')
# print(soup.prettify())

# soup_children = list(soup.children)
html = list(soup.children)[2]
body = list(html.children)[3]
p = list(body.children)[1]
p_text = p.get_text()

# finding all instances of a tag
p_tags = soup.find_all('p')

# finding the first instance of a tag
first_p_tag = soup.find('p')

# searching for tags by class and id (using different web page)
response = requests.get(
    "http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
soup = BeautifulSoup(response.content, 'html.parser')

outer_text_p_tags = soup.find_all('p', class_='outer-text')
outer_texts = soup.find_all(class_='outer-text')
first_ids = soup.find_all(id='first')

# find by css selector
div_and_p = soup.select('div p')

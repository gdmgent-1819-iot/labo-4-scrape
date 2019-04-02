# Example: download a file using requests + beautifulsoup
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'http://web.mta.info/developers/turnstile.html'

response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')
links = html.findAll('a')
test_a_tag = links[36]
link = test_a_tag['href']

dl_url = 'http://web.mta.info/developers/' + link
urllib.request.urlretrieve(dl_url, './' + link[link.find('/turnstile_')+1:])

time.sleep(1)

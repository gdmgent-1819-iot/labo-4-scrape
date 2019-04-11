import requests
import random
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def proxies_pool():
    url = 'https://www.sslproxies.org/'
    # retrieve page
    with requests.Session() as res:
        proxies_page = res.get(url)
    # create BeautifulSoup object & find table element containing proxies
    soup = BeautifulSoup(proxies_page.content, 'html.parser')
    proxies_table = soup.find(id='proxylisttable')
    # go through rows in table & store in right format
    proxies = []
    for row in proxies_table.tbody.find_all('tr'):
        proxies.append('{}:{}'.format(row.find_all('td')[
                       0].string, row.find_all('td')[1].string))
    return proxies


proxies = proxies_pool()

# dict of accept headers for each user agent
accepts = {"Firefox": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           "Safari, Chrome": "application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5"}
# get a random user-agent using fake_useragent package
ua = UserAgent()
if random.random() > 0.5:
    random_user_agent = ua.chrome
else:
    random_user_agent = ua.firefox

valid_accept = accepts['Firefox'] if random_user_agent.find(
    'Firefox') > 0 else accepts['Safari, Chrome']
headers = {'User-Agent': random_user_agent, 'Accept': valid_accept}

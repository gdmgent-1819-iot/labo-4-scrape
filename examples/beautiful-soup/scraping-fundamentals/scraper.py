from bs4 import BeautifulSoup
import urllib.request
import csv

url = 'http://www.fasttrack.co.uk/league-tables/tech-track-100/league-table'

# store html from url
response = urllib.request.urlopen(url)

# parse & store html w/ beautifulsoup
soup = BeautifulSoup(response, 'html.parser')

# find results within table
table = soup.find('table', attrs={'class': 'tableSorter'})
results = table.find_all('tr')
print('Numer of results', len(results))

# create & write headers to a list
rows = []
rows.append(['Rank', 'Company Name', 'Web page', 'Description', 'Location',
             'Year end', 'Annual sales rise over 3 years', 'Sales $000s', 'Staff', 'Comments'])
print(rows)

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://tripadvisor.fr')
bs = BeautifulSoup(html.read(), 'html.parser')

print('Locations:')
nameList = bs.findAll('div', {'class': 'Ffh78ncj _2g-v5ZyD _3auwW4vL _3XQY3qGv'})
for name in nameList:
    print(name.get_text())

print('Destinations:')
nameList = bs.findAll('div', {'class': 'Ffh78ncj _2g-v5ZyD _3-OVWReS _3XQY3qGv'})
for name in nameList:
    print(name.get_text())
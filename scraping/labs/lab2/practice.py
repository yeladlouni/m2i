from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://tripadvisor.fr')
bs = BeautifulSoup(html.read(), 'html.parser') # lent et intolérant aux erreurs de syntaxe à l'intérieur de la page HTML
#bs = BeautifulSoup(html.read(), 'lxml') # rapide et tolérant aux erreurs de syntaxe HTML
#bs = BeautifulSoup(html.read(), 'html5lib') # lent et tolérant aux erreurs de syntaxe HTML

html = urlopen('file:///C:\\Users\\yelad\\PycharmProjects\\m2i\\scraping\\labs\\lab2\\test.html')


bs = BeautifulSoup(html.read(), 'html5lib')
print(bs.div)

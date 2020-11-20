import requests
from bs4 import BeautifulSoup

r = requests.get('https://query2.finance.yahoo.com/v10/finance/quoteSummary/GLW?formatted=true&crumb=8ldhetOu7RJ&lang=en-US&region=US&modules=summaryDetail&corsDomain=finance.yahoo.com')

data = r.json()

print(data)
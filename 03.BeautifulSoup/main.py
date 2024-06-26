import requests
from bs4 import BeautifulSoup

r = requests.get('https://wusandwitch.github.io/20240705_ExampleSite/example.html')

soup = BeautifulSoup(r.text, 'html.parser')

for item in soup.find_all('li'):
    fruit = item.find('h1').text
    price = item.find('p').text
    
    print(fruit, price)
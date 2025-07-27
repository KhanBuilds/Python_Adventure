import http
import requests
from bs4 import BeautifulSoup
 
url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text , 'html.parser')
tags = soup.find_all('a', class_='tag')

for tag in tags :
    if tag.text.strip().lower() == 'inspirational':
        inspirational_url = url + tag['href']
        print("Inspirational URL: ", inspirational_url)

        response_inspirational = requests.get(inspirational_url)
        soup_inspirational = BeautifulSoup(response_inspirational.text , 'html.parser')
        quotes = soup_inspirational.find_all('span', class_='text')
        for quote in quotes:
            print(quote.text.strip())
        break

#importing necessary libraries
import http
import requests
from bs4 import BeautifulSoup

 #Setting the URL to scrape 
url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text , 'html.parser')
tags = soup.find_all('a', class_='tag')

#In here we are looking for the inpirational tag in a class of tags 'a' and then we are getting the href link of the inspirational tag

for tag in tags :
    if tag.text.strip().lower() == 'inspirational':

        #The href link is relative and needs to be combined with the base URL to get the full URL
        inspirational_url = url + tag['href']

        #Printing the inspirational URL jusr to check if we are getting the correct URL
        print("Inspirational URL: ", inspirational_url)

        #Now we are sending a GET request to the inspirational URL and parsing the response using BeautifulSoup
        response_inspirational = requests.get(inspirational_url)

        #Parsing the response using BeautifulSoup
        soup_inspirational = BeautifulSoup(response_inspirational.text , 'html.parser')

        #This looks for the clas 'text' which are stored in a span tag and then we are getting the text of the quotes

        quotes = soup_inspirational.find_all('span', class_='text')

        #This loops through the quotes and prints them out
        for quote in quotes:
            print(quote.text.strip())
        break

#importing necessary libraries
import http
import requests
from bs4 import BeautifulSoup

 #Setting the URL to scrape 
url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text , 'html.parser')

#This looks for the class 'tag' which is stored in a tag and then we are getting the text of the tags
tags = soup.find_all('a', class_='tag')


user_input = input("Enter the tag you want to scrape: ")
for tag in tags :
    if tag.text.strip().lower() == user_input.strip().lower():

        #The href link is relative and needs to be combined with the base URL to get the full URL
        user_url = url + tag['href']

        #Printing the inspirational URL jusr to check if we are getting the correct URL
        print("Inspirational URL: ", user_url)

        #Now we are sending a Get request to the user URL and parsing the response using BeautifulSoup
        response_user = requests.get(user_url)

        #Parsing the response using BeautifulSoup
        soup_user = BeautifulSoup(response_user.text , 'html.parser')

        #This looks for the class 'text' which is stored in a span tag and then we are getting the text of the quotes

        quotes = soup_user.find_all('span', class_='text')

        #This loops through the quotes and prints them out
        for quote in quotes:
            print(quote.text.strip())
        break

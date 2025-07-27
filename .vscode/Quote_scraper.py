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
user_input = input("Enter the tag you want to scrape: ")
for tag in tags :
    
    #Checking if the tag text is matching user input and if it is then we are getting the href link of the inspirational tag
    if tag.text.strip().lower() == user_input.strip().lower():

        #The href link is relative and needs to be combined with the base URL to get the full URL
        user_url = url + tag['href']

        #Printing the user input URL jusr to check if we are getting the correct URL
        print("Inspirational URL: ", user_url)

        #Now we are sending a GET request to the user input URL and parsing the response using BeautifulSoup
        response_user = requests.get(user_url)

        #Parsing the response using BeautifulSoup
        soup_user = BeautifulSoup(response_user.text , 'html.parser')

        #This looks for the clas 'text' which are stored in a span tag and then we are getting the text of the quotes

        quotes = soup_user.find_all('span', class_='text')

        #This loops through the quotes and prints them out
        for quote in quotes:
            print(quote.text.strip())
        break

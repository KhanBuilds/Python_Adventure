import requests
API_KEY = "e3ZA9tEzJG3yhcLHPw6kVzKKZ1VgW7VCzPWQlE4C" #bro stop looking for api keys BE BETTER


news_url = f"https://api.thenewsapi.com/v1/news/top?api_token={API_KEY}&locale=us&limit=3&search=apple-inc"
news_response = requests.get(news_url)
news_data = news_response.json()
story = news_data.get("data", [])[0].get("description", "")
print(story)


    


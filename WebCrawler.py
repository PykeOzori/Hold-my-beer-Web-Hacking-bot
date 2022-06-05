# Imports required libraries
import requests
from bs4 import BeautifulSoup
# Asks for user input and crawls the website
URLinput = input("Website: ")
URL = requests.get("https://" + URLinput)
URL.request.url
print(URL.request.url)
soup = BeautifulSoup(URL.content, 'html.parser')
Links = soup.find_all('a')
for Links in soup.find_all('a'):
    print(Links.get('href'))

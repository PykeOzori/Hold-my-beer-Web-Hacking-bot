# Imports required libraries
import requests
from bs4 import BeautifulSoup
# Asks for user input
URL_input = input("Website: ")
URL = "https://" + URL_input
# Crawls the website
def Crawl(URL):
    URL_Request = requests.get(URL)
    URL_Result = URL_Request.content
    URL_set = set()
    soup = BeautifulSoup(URL_Result, 'html.parser')
    Links = soup.find_all('a')
    for Links in soup.find_all('a'):
        Results = Links.get('href')
        if Results == None:
            continue

        if 'http' not in Results:
            Results = URL + Results

        if URL_input not in Results:
            continue
        URL_set.add(Results)
        for URL in URL_set:
            print(URL)
    return URL_set
URL_Set = Crawl(URL)
for URL in URL_Set:
    Crawl(URL)
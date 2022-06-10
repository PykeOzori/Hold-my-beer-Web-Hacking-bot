# Imports required libraries
import requests
from bs4 import BeautifulSoup

# Crawls the website
def crawl(url, domain):
	"""
	Crawls and prints all links on the provided URL.
	Only URL that match the domain will be included

	Args:
		url (string): The URL to crawl
		domain (list): The domain to verify URLS for

	Returns:
		list: A list of all found URL
	"""
	
	# Request and parse page
	url_request = requests.get(url)
	soup = BeautifulSoup(url_request.content, 'html.parser')
	url_set = set()

	# Find all achor tags in page and get the "href" attribute
	for links in soup.find_all('a'):
		results = links.get('href')
		if results == None:
			continue

		if 'http' not in results:
			results = url + results

		if domain not in results:
			continue
		
		url_set.add(results)

	return list(url_set)
	
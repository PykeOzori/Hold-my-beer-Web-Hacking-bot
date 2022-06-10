# Imports required libraries
import requests
from bs4 import BeautifulSoup

def find_urls(url):
	"""
	Find all anchor links on a URL.

	Args:
		url (string): The URL to crawl

	Returns:
		list: A list links found on the page
	"""

	url_request = requests.get(url)
	soup = BeautifulSoup(url_request.content, 'html.parser')

	return soup.find_all('a')

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
	
	# TODO: Follow further links with limit (loop) OR depth level (recursion)
	url_set = set()

	for links in find_urls(url):
		results = links.get('href')
		if results == None:
			continue

		if 'http' not in results:
			results = url + results

		if domain not in results:
			continue
		
		url_set.add(results)

	return list(url_set)
	
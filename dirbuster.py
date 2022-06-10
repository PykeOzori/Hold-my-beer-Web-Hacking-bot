import pydirbuster
import requests
from bs4 import BeautifulSoup

def verify_domain(domain):
	"""
	Verifies if a domain can be reached over HTTP or HTTPS and
	returns the full URL or None if the website is offline.

	Args:
		domain (string): The domain to verify

	Returns:
		String|None: URL of online website
	"""

	url = None

	try:
		# See if we can reach domain over HTTP or HTTPS
		request = requests.get('http://'+domain)

		if request.status_code == 301:
			request = requests.get('https://'+domain)
			url = 'https://'+domain
		else: 
			url = 'http://'+domain

		# Only succeed if the status code is 200
		if request.status_code != 200:
			url = None
	except:
		print("Domain does not exist")
	
	return url

def filter_results(results):
	"""
	Filters out results of Dirbuster for easier data handling.

	Args:
		results (dict): Raw dirbuster result

	Returns:
		dict: Cleaned up results
	"""

	filtered_results = []

	# Only successful status codes:
	# See: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
	for status_code in range(200, 300):
		if len(results[status_code]) > 0:
			filtered_results = filtered_results + results[status_code]

	return filtered_results

def create_urls(url, results):
	"""
	Take all result paths from brute forcing and append to the URL:

	Example:
		"robots.txt" becomes "https://example.com/robots.txt"

	Args:
		url (string): The URL to prepend to the result
		results (list): The list of discovered results

	Returns:
		list: A list of full URL
	"""

	new_urls = []

	for result in results:
		new_urls.append(f"{url}/{result}")

	return new_urls

def run(url):
	"""
	Run the dirbuster library (https://pypi.org/project/pydirbuster/) and will prompt for
	user imput.

	Args:
		url (string): The URL to run dirbuster on

	Returns:
		dict: Dirbuster scan results
	"""

	# TODO: See if file exists or use try/catch
	wordlist = input("Path to wordlist: ")

	webbuster = pydirbuster.Pybuster(
		url=url,
		wordfile=wordlist,
		exts=[] # php, html
	)
	webbuster.Run()

	found_urls = filter_results(webbuster.results)
	found_urls = create_urls(url, found_urls)

	return found_urls

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

def clean_results(results):
	"""
	Filters out results of Dirbuster for easier data handling.

	Args:
		results (dict): Raw dirbuster result

	Returns:
		dict: Cleaned up results
	"""

	# TODO: Only get 200 status codes or clean up results
	return results

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

	return clean_results(webbuster.results)

# Crawler part

# Imports required libraries

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

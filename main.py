import sys
import os
import requests
from dirbuster import run

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

def main():
	print("Jelle's awesome web scanner!")

	# Verify domain
	domain = input("Website: ")
	url = verify_domain(domain)
	if url is None:
		sys.exit()

	# Verify wordlist
	wordlist = input("Path to wordlist: ")
	wordlist_exists = os.path.exists(wordlist)
	if not wordlist_exists:
		sys.exit("Oh no, no file!")

	results = run(url, wordlist)
	print(results)


if __name__ == "__main__":
	main()
import pydirbuster

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

def run(url, wordlist):
	"""
	Run the dirbuster library (https://pypi.org/project/pydirbuster/) and will prompt for
	user imput.

	Args:
		url (string): The URL to run dirbuster on
		wordlist (string): The wordlist to use

	Returns:
		dict: Dirbuster scan results
	"""

	webbuster = pydirbuster.Pybuster(
		url=url,
		wordfile=wordlist,
		exts=[] # php, html
	)
	webbuster.Run()

	found_urls = filter_results(webbuster.results)
	found_urls = create_urls(url, found_urls)

	return found_urls

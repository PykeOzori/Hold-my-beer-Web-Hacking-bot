import sys
import os
from dirbuster import verify_domain, run

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

	results = run(url)
	print(results)


if __name__ == "__main__":
	main()
import sys
from dirbuster import verify_domain, run

def main():
	print("Jelle's awesome web scanner!")

	domain = input("Website: ")
	url = verify_domain(domain)

	if url is None:
		sys.exit()

	results = run(url)
	print(results)


if __name__ == "__main__":
	main()
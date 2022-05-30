import sys
import pydirbuster
import requests

website_online = False
request = None
URL = input("Website: ")
try:
	request = requests.get('http://'+URL)
	if request.status_code == 301:
		request = requests.get('https://'+URL)
		URL = 'https://'+URL
	else: 
		URL = 'http://'+URL

	if request.status_code == 200:
		website_online = True
	
except:
	print("Domain does not exist")
	sys.exit()

if website_online == False:
	print("Website is not online")
	sys.exit()

print(request.status_code)


def main():
	print("[Pybuster test]")

	webbuster = pydirbuster.Pybuster(
		url=URL,
		wordfile="wordlist.txt",
		exts=[] # php, html
	)


	print(webbuster.results)

if __name__ == "__main__":
	main()

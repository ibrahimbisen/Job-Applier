#import Beautiful Soup
from bs4 import BeautifulSoup
import requests
# var cookies = require('./cookies');

#retreive url to search
page_url = input("Enter URL: ")
mainSite = "https://www.glassdoor.com"

#requests page through User Agent Mozilla
page_response = requests.get(page_url,  headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(page_response.content, "html.parser")

# All Easy Apply Jobs
i = 1
for job in soup.find_all("li", attrs={"data-is-easy-apply":"true"}):

	print("Job Number:", i)
	sess = requests.Session()
	easyApply_url = mainSite + job.find("a", attrs={"class":"jobLink"})["href"]
	easyApply_response = sess.get(easyApply_url, headers={'User-Agent': 'Mozilla/5.0'})
	curPage = BeautifulSoup(easyApply_response.content, "html.parser")
	print(easyApply_url)
	curPage = BeautifulSoup(easyApply_response.content, "html.parser")
	#write links to file
	f = open("scraped_app_links.txt", "a")
	f.write("Job Number: "+ str(i) + '\n')
	f.write(easyApply_url+'\n')
	f.write('\n')
	i=+1

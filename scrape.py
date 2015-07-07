from bs4 import BeautifulSoup
from datetime import timedelta, date
import requests

"""Constants"""
start_date = date(2015, 6, 1)
end_date = date(2015, 6, 5)
base = "http://redditarchive.com/?d="
"""Constants"""

f = open("output.txt", "w", 10)
def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

def main():
	for single_date in daterange(start_date, end_date):
	    arg = single_date.strftime("%B+%d,+%Y")
	    parseIndex(base+arg)


def parseIndex(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.text)
	titles = soup.findAll('a', {'class': 'i_title'})
	for title in titles:
		text = title.text.encode('ascii', 'ignore').strip()
		if text.startswith("TIL "):
			print text
			f.write(text + "\n")



if __name__ == "__main__":
    main()

import urllib3
from bs4 import BeautifulSoup
http = urllib3.PoolManager()
url = 'http://quotes.toscrape.com/'
r = http.request("GET", url)

tetx = open("crap.txt", "w")
soup = BeautifulSoup(r.data, 'html.parser')
print("Title:")
print(soup.title)
url2 = " "
url = 'http://quotes.toscrape.com/'
url1 = 'http://quotes.toscrape.com/'
b = 0
page = 1
while b == 0:
    print("-" * 5, "Page", page, "-" * 5)
    tetx.write(str("-" * 5) + "Page" + str(page) + str("-" * 5) +"\n")

    http = urllib3.PoolManager()
    r = http.request("GET", url)
    soup = BeautifulSoup(r.data, 'html.parser')

    rez = soup.find_all("div", attrs={"class": "quote"})
    authors = soup.find_all("div", attrs={"class": "quote"})

    for i, quote in enumerate(rez):
        main_text = quote.find("span", attrs={'class': "text"})
        author_text = authors[i].find("small", attrs={'class': "author"})
        print(i + 1, main_text.text[1:-1], "by", author_text.text)
        tetx.write(str(i + 1 ) + " " + main_text.text[1:-1] + " by "+ author_text.text + "\n")

    for next in soup.find_all("li", attrs={"class": "next"}):
        for next1 in next.find_all("a"):
            tt = next.find_all('a', href = True)
            url2 = next1.get('href')
            url = url1 + url2[1::]
            page += 1
    if not next in soup.find_all("li", attrs={"class": "next"}):
        b = 1
        print("All page scraped")
        tetx.close()
